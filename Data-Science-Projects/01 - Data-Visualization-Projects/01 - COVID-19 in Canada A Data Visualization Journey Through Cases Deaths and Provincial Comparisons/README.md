# 📊 COVID-19 in Canada: A Data Visualization Journey through Cases, Deaths, and Provincial Comparisons

## 📌 Project Overview

This project explores the impact of the **`COVID-19`** pandemic in **`Canada`** through an in-depth **`data visualization`** journey. It highlights trends in confirmed **`cases`** and **`deaths`** while drawing comparisons across **`provinces`**. The project aims to provide a comprehensive understanding of **regional disparities** and **temporal trends** during the pandemic.

## 📂 Repository Structure

The project is meticulously organized for seamless exploration:

+ **[Notebook](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/01%20-%20Data-Visualization-Projects/01%20-%20COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons/01%20-%20Notebooks):** Contains the Jupyter Notebook, "[COVID-19 in Canada: A Data Visualization Journey Through Cases, Deaths, and Provincial Comparisons](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/01%20-%20Data-Visualization-Projects/01%20-%20COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons/01%20-%20Notebooks/COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons.ipynb)", documenting each step of the **analysis**, from **`data preparation`** to **insightful `visualizations`** and **findings**.
+ **[Data](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/01%20-%20Data-Visualization-Projects/01%20-%20COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons/02%20-%20Data):** Houses the primary dataset, [canada_covid19.csv](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/01%20-%20Data-Visualization-Projects/01%20-%20COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons/02%20-%20Data/canada_covid19.csv), used throughout the project. This dataset, obtained from the [Government of Canada Public Health Infobase](https://open.canada.ca/data/en/dataset/261c32ab-4cfd-4f81-9dea-7b64065690dc), includes daily reported **`COVID-19 cases`** and **`cumulative deaths`** for all Canadian **`provinces`** and territories.
+ **[Visualizations](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/01%20-%20Data-Visualization-Projects/01%20-%20COVID-19%20in%20Canada%20A%20Data%20Visualization%20Journey%20Through%20Cases%20Deaths%20and%20Provincial%20Comparisons/03%20-%20Visualizations):** Features exported **graphs** and **charts** generated during the analysis, providing a clear and comprehensive view of the **pandemic's trends** and **regional disparities**.

## 📊 Dataset Description

+ **Source:** **`COVID-19 cases`** and **`death`** data compiled from **official Canadian provincial and territorial health reports**, sourced from the [Government of Canada Public Health Infobase](https://open.canada.ca/data/en/dataset/261c32ab-4cfd-4f81-9dea-7b64065690dc).
  
+ **Size:**
  
  + **3180 `rows`**, covering daily reports for **13 provinces** from **`February 2020`** to **`May 2021`**.
  + **7 `columns`:** 
    + **`prname`:** Represents the **name** of the **`province`** in **`Canada`** where the data was collected (e.g., **`British Columbia`**, **`Alberta`**, **`Ontario`**).
    + **`date`:** The date of the **reported data** in the format **`YYYY-MM-DD`**. Covers the **timeline** of the **`COVID-19`** pandemic in **`Canada`**, from **`February 2020`** to **`May 2021`**.
    + **`reporting_week`:** Indicates the **week of the year** during which the data was reported. Range: **1–53**, corresponding to the **ISO week numbers**.
    + **`totalcases`:** **Cumulative** count of confirmed **`COVID-19 cases`** reported in the respective **`province`** up to the given date.
    + **`ratecases_total`:** The **cumulative rate** of confirmed **`cases`** per **100,000** population in the respective **province**.
    + **`numdeaths`:** **Cumulative** count of **`deaths`** attributed to **`COVID-19`** in the respective **`province`** up to the given date.
    + **`ratedeaths`:** The **cumulative rate** of **`deaths`** per **100,000** population in the respective **`province`**.
    
+ **Key Statistics:**
  
  + **`Total cases`** reported: **1,370,000+**.
  + **`Total deaths`** reported: **25,000+**.
  + **Missing data:** **6.7%** in **`ratecases_total`** and **`ratedeaths`**.

## 💡 Key Insights & Findings

+ **National Trends:**

  + Canada saw the **highest surge** in **cases** during the **second wave** (**`November 2020–January 2021v**), peaking at over **7,000** daily cases nationwide.
  + **`December 2020`** recorded the **highest death** toll, with **3,000+** deaths in a single month.
    
+ **Provincial Analysis:**

  + **`Ontario`** and **`Quebec`** contributed to **65%** of **`total cases`** and **70%** of **`deaths`** in Canada.
  + **`Nunavut`**, **`Yukon`**, and the **`Northwest Territories`** had **less** than **1,000 cases** combined, highlighting the disparity in COVID-19's impact.
    
+ **Temporal Patterns:**

  + The **first wave** began in **`March 2020`**, with **`cases`** **growing steadily** until **`May 2020`**.
  + **Subsequent waves** showed **higher peaks** and **longer durations**, reflecting increased community transmission.

+ **Mortality Rates:**

  + **`Quebec`** had the **highest `death rate`**, with **4.5** deaths per **100,000** population.
  + Other provinces, such as **`British Columbia`** and **`Alberta`**, maintained **lower `death rates`** despite high case counts.

## 🔑 Conclusion

This project demonstrates how effective **`data visualization`** can uncover significant insights into the dynamics of a pandemic. By exploring **regional disparities** and **national trends**, it provides valuable perspectives for **public health policymakers** and **researchers**. The findings underline the need for tailored responses to public health crises, considering both **regional** and **temporal** factors.
