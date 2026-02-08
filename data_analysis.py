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

"""

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

"""

""" Notes:
The Dates are stored as strings --> Convert to datetime objects so I can work with them (analyse trends overtime)
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
sns.barplot(data=spend_by_market, x='Market', y='Spend_USD', hue='Market', palette='viridis')

# Add title and labels to the axes
plt.title('Total Ad Spend by Market (Historic)')
plt.ylabel('Total Spend (USD)')
plt.xlabel('Market')

# Format the y-axis with commas for thousands (e.g. 1,000,000 instead of 1000000)
current_values = plt.gca().get_yticks() # Get the current y-axis tick values (tick values are the numbers on the y-axis)
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values]) # Format the tick labels with commas

# Show the plot
plt.show()