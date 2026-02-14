# --- Setup & Imports ---

# Import Libraries
import pandas as pd # For data tables (dataframes) that we can manipulate
import numpy as np # For numerical operations
import matplotlib.pyplot as plt # For plotting data on graphs
import seaborn as sns # For making prettier graphs

# Load the data from CSV files into pandas dataframes
historic_df = pd.read_csv('Historic Campaign Data - Sheet1.csv')
brand_lift_df = pd.read_csv('Brand Lift Study Results - Sheet1.csv')
creative_df = pd.read_csv('Creative Performance Report - Sheet1.csv')



# Inspect the data
# We look at the first few rows (.head) and data types (.info)
print("--- 1. Historic Campaign Data ---")
print(historic_df.info()) # Get an overview of the data types and missing values
print(historic_df.head()) # Print the first few rows to see what the data looks like

print("--- 2. Brand Lift Study Results ---")
print(brand_lift_df.info())
print(brand_lift_df.head())

print("--- 3. Creative Performance Report ---")
print(creative_df.info())
print(creative_df.head())



""" Notes:
The Dates are stored as strings --> Convert to datetime objects so we can work with them (analyse trends overtime)
"""


# Convert Date columns to datetime objects
historic_df['Week_Start'] = pd.to_datetime(historic_df['Week_Start'])
creative_df['Report_Date'] = pd.to_datetime(creative_df['Report_Date'])

# Checking the SPEND BY MARKET (Where is our budget going?)
# Group the data by 'Market' and sum the 'Spend_USD' for each market, and reset the index to get a clean dataframe
spend_by_market = historic_df.groupby('Market')['Spend_USD'].sum().reset_index()

print("\n--- Spend by Market ---")
print(spend_by_market)

# Bar Chart
# Set the size of the graph (10 inches wide, 6 inches tall)
plt.figure(figsize=(10,6))

# Create a bar plot using Seaborn
# x = the categories (Market), y = the values (Spend_USD), hue = color by Market, palette = color scheme (make it look nice)
# Seaborn turns the Dataframe into a bar chart
sns.barplot(data=spend_by_market, x='Market', y='Spend_USD', hue='Market', palette='viridis')

# Add title and labels to the axes
# plt draws the graph defined by the previous sns.barplot line
plt.title('Total Ad Spend by Market (Historic)')
plt.ylabel('Total Spend (USD)')
plt.xlabel('Market')

# Format the y-axis with commas for thousands (e.g. 1,000,000 instead of 1000000)
current_values = plt.gca().get_yticks() # Get the current y-axis tick values (tick values are the numbers on the y-axis)
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values]) # Format the tick labels with commas

# Show the plot
plt.show()

# ==================================================================================
# Calculate CPA (Cost Per Acquisition)
# ==================================================================================
# How much does it cost to get each person to convert? - Efficiency of our ad spend
# CPA = Total Spend / Total Conversions             (Lower CPA = Better Performance)


# Organise the data into groups (a unique group for each possible combination of Market and Channel)
grouped_data = historic_df.groupby(['Market','Channel'])

# Select the relevant columns for CPA analysis (Spend and Conversions) from the grouped data
# Double [] to send a list of columns we want to keep - To keep it a dataframe instead of a series
relevant_columns = grouped_data[['Spend_USD','Conversions']]

# Sum the Spend and Conversions for each group (Market + Channel)
cpa_analysis = relevant_columns.sum().reset_index()

# Calculate CPA for each group (Market + Channel) - Create a new column 'CPA' to store our results
cpa_analysis['CPA'] = cpa_analysis['Spend_USD'] / cpa_analysis['Conversions']

cpa_analysis = cpa_analysis.sort_values('CPA', ascending=True) # Sort the results by CPA in ascending order (lowest CPA at the top)

print("\n\033[32m--- CPA by Market and Channel ---\033[0m")

print(cpa_analysis)

# ==================================================================================
# Visualise CPA by Market and Channel (Bar Chart)
# ==================================================================================

plt.figure(figsize=(12,6)) # Set the size of the graph

# Create a bar chart with Market on the x-axis, CPA on the y-axis, and different colors for each Channel
sns.barplot(data=cpa_analysis, x='Market', y='CPA', hue='Channel', palette='rocket')

# Add title and labels to the axes
plt.title('Cost Per Acquisition (CPA) by Market & Channel')
plt.ylabel('Cost per User (USD)')
plt.xlabel('Market')
plt.legend(title='Channel') # Add a legend to explain the colors (hue) with the title 'Channel'

plt.show()

# ==================================================================================
# CPLU Analysis (Cost Per Lifted User)
# ==================================================================================

# CPA measures 'Action' (Did they click buy?)
# CPLU measures 'Influence' (Did we change their mind?)
# Because changing their mind could lead to a conversion later on (so we can't solely rely on CPA to measure the impact of our ads)

# Group the data by Campaign Name, Market, and Channel (to get a unique group/row for each combination of these 3 variables)
groups_to_be_summed = historic_df.groupby(['Campaign_Name', 'Market','Channel'])
# Sum the Spend and Reach for each group (Reach is used to calculate the Lifted Users later)
historic_totals = groups_to_be_summed[['Spend_USD','Reach']].sum().reset_index()


# --------- MERGE DATASETS (Inner Join) ---------

# INNER JOIN tables 'brand_lift_df' and 'historic_totals' using the composite key of ['Campaign_Name', 'Market','Channel']
# Only combine rows where ALL THREE of these columns match in both tables (inner join)
cplu_df = pd.merge(brand_lift_df, historic_totals, on=['Campaign_Name', 'Market','Channel'], how='inner')


# --------- CALCULATE Absolute Lift ---------
# Absolute Lift = Exposed Rate - Control Rate (How much did the ad influence the exposed group compared to the people who didn't see the ad ('Control' group)?)
cplu_df['Absolute_Lift'] = cplu_df['Exposed_Rate'] - cplu_df['Control_Rate']

# --------- CALCULATE Lifted Users ---------
# How many actual users changed their mind because of the ad?
# Lifted Users = Reach(How many people saw the ad) * Absolute Lift (Success rate of the ad)
cplu_df['Lifted_Users'] = cplu_df['Reach'] * cplu_df['Absolute_Lift']

# --------- CALCULATE Cost Per Lifted User (CPLU) ---------
# CPLU = Total Spend / Lifted Users (How much did it cost to change the mind of each user?)
cplu_df['CPLU'] = cplu_df['Spend_USD'] / cplu_df['Lifted_Users']

# Sort the results by CPLU in ascending order (lowest CPLU at the top)
cplu_sorted = cplu_df.sort_values('CPLU', ascending=True)

print("\n\033[32m--- Cost Per Lifted User (CPLU) by Campaign, Market & Channel ---\033[0m")
print(cplu_sorted[['Campaign_Name', 'Market', 'Channel', 'CPLU', 'Lifted_Users']])

# ==================================================================================
# Visualise CPLU by Market and Channel (Bar Chart)
# ==================================================================================

plt.figure(figsize=(12,6)) # Set the size of the graph
# Create a bar chart with Market on the x-axis, CPLU on the y-axis, and different colors for each Channel
sns.barplot(data=cplu_sorted, x='Market', y='CPLU', hue='Channel', palette='magma')

# Add title and labels to the axes
plt.title('Cost Per Lifted User (CPLU) by Market & Channel')
plt.ylabel('Cost per Lifted User (USD)')
plt.xlabel('Market')
plt.show()

# ==================================================================================
# Test for Statistical Significance (The Z-Test)
# ==================================================================================

# Import the Z-Test function to check if the data is statistically significant (Is the difference in conversion rates between the exposed and control groups due to the ad, or just random chance?)
from statsmodels.stats.proportion import proportions_ztest

# Define a function to calculate the p-value (statistical significance) for each row of the brand lift data (for each campaign, market, and channel)
def calculate_significance(row):

    # Create a numpy array of the "Successes" (People who liked the brand with or without the ad)
    successes = np.array([row['Exposed_Consideration'], row['Control_Consideration']])

    # Create a numpy array of the "Trials" (Total people in the exposed and control groups)
    trials = np.array([row['Exposed_Responses'], row['Control_Responses']])

    # Perform the Z-Test using the proportions_ztest function)
    stat, p_value = proportions_ztest(successes, trials, alternative='larger')

    # Return the p-value (We will use this to determine if the results are statistically significant)
    return p_value

# Use .apply() to run the function on every row of the brand_lift_df dataframe
# Create a new column 'P_value' to store the results
brand_lift_df['P_value'] = brand_lift_df.apply(calculate_significance, axis=1) # axis=1 means we apply the function to each row (instead of each column)

# DETERMINE SIGNIFICANCE
# If the p-value is less than 0.05, we consider the result statistically significant (the ad had a real impact on brand consideration)
brand_lift_df['Significant'] = brand_lift_df['P_value'] < 0.05


print("\n\033[32m--- Brand Lift Study Results with Statistical Significance ---\033[0m")
print(brand_lift_df[['Campaign_Name', 'Market', 'Channel', 'Relative_Lift', 'Significant']].sort_values('Relative_Lift', ascending=False))

# ==================================================================================
# Creative Performance Analysis (The last csv file)
# ================================================================================== 


