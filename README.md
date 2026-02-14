# Google Step Up Challenge: Gemini Pro Launch Strategy 🚀

**Role:** Data Scientist & Data Strategist (Combined Route)  
**Tools:** Python (Pandas, Seaborn, Statsmodels), PowerPoint, Excel  
**Outcome:** Projected **4x growth** in user acquisition with a **90% reduction** in CPA.

---

## 📖 Overview
This repository contains my submission for the **Google Step Up Challenge** (hosted by Digdata). The objective was to design a data-driven marketing strategy to launch **Gemini Pro** to university students across multiple international markets with a budget of **$10M USD**.

I undertook the **Combined Route**, executing the full data lifecycle:
1.  **Data Science:** Cleaning, analyzing, and testing historic campaign data using Python.
2.  **Data Strategy:** Translating insights into a high-efficiency budget allocation plan.

---

## 📊 Key Results
By analyzing historic performance and "Brand Lift" studies, I identified major inefficiencies in the European market and high-growth opportunities in the Middle East.

* **Acquisition Cost:** Reduced from **~$30.00** to **~$3.20** (90% reduction).
* **Sign-ups:** Projected increase from **300k** (historic baseline) to **1.2M** (forecast).
* **Brand Impact:** Pivoted spend from "Statistically Insignificant" channels (UK Display) to high-impact channels (Egypt YouTube).
* **Engagement:** Identified creative concepts that drove **19x higher** consideration scores among the 18-24 demographic.

---

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| `data_analysis.py` | **The Code.** Python script containing the full analysis pipeline: data cleaning, CPA calculations, Z-Tests for statistical significance, and visualization generation. |
| `Google_Step_Up_Challenge_As-Samee_Clayton.pdf` | **The Strategy.** The final executive presentation delivered to Google stakeholders. Contains the business case, visualizations, and budget roadmap. |

> **⚠️ Note on Data Access:**
> This repository contains the analysis logic and strategy. The raw data files (`.csv`) are proprietary and have been excluded via `.gitignore` to protect confidentiality. The Python script demonstrates the methodology used to derive the insights found in the PDF presentation.

---

## 💡 Methodology

### 1. Data Science Phase (Python)
I utilized **Pandas** for data manipulation and **Seaborn** for visualization. Key technical actions included:
* **Statistical Significance Testing:** Implemented `statsmodels.stats.proportion.proportions_ztest` to filter out "random noise" from Brand Lift studies.
* **Efficiency Analysis:** Calculated **CPA** (Cost Per Acquisition) and **CPLU** (Cost Per Lifted User) to measure the true ROI of every dollar spent.
* **Creative Heatmapping:** Analyzed creative performance across age groups to identify the highest-resonating content.

### 2. Strategic Phase (Business Logic)
Based on the data, I developed a "High-Efficiency Growth" strategy:
* **The Cut:** Eliminated the $2.50+ CPLU "Display" channel in the UK/DE (proven ineffective).
* **The Pivot:** Reallocated **70% of the budget ($7M)** to Search & YouTube in Egypt and Saudi Arabia, capitalizing on a $0.21 CPLU.
* **The Creative:** Recommended replacing "Sales-heavy" ads with "Utility-focused" content (Life Hacks), which data showed performed 1,800% better.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`
* **Analysis:** Hypothesis Testing (Z-Test), Regression Analysis, Data Visualization

---

**Author:** As-Samee Clayton  
**University:** Durham University