# Financial Efficiency and Performance Metrics Analysis of European Football Leagues

## 📌 Project Overview

This project examines financial efficiency and performance metrics of football teams across 15 European leagues, providing a comprehensive Exploratory Data Analysis (EDA). It explores how financial spending impacts team performance, identifies patterns over time, and offers valuable insights through an interactive dashboard. This analysis addresses key questions surrounding financial efficiency, strategic spending, and performance dynamics across different leagues.

## 📂 Repository Structure

This project is organized into five main folders: Proposal, Notebooks, Data, Dashboard, and Presentation. The structure is as follows:

### [Proposal](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/01%20-%20Proposal)

This folder contains the project proposal, outlining the objectives, methodology, and deliverables for analyzing financial and performance metrics of football teams across European leagues. It includes the approved project proposal file:

+ **[Project Proposal](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/01%20-%20Proposal/Project%20Proposal.pdf):** This PDF represents the proposal of the Final Capstone Project, which has been accepted along with its outlined plan. The project involves an in-depth Exploratory Data Analysis (EDA) of financial and performance metrics for football teams across 15 European leagues. The goal is to explore how financial spending correlates with team performance, identify trends over time, and provide insights through an interactive dashboard. The dataset includes financial information like revenue and spending, and performance data such as goals, wins, and losses. The analysis will help answer key questions about financial efficiency and performance across different leagues.

### [Notebooks](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks)

This folder contains the analysis of financial and performance metrics across European football leagues, detailing data collection, cleaning, validation, and exploratory data analysis steps. It includes the following notebooks:

**1. [Notebook_1_Data_Collection](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks/Notebook_1_Data_Collection.ipynb):** This notebook is the first step in a project analyzing the correlation between financial investment and performance in European football clubs. It focuses on data collection through web scraping from the Transfermarkt website. The target dataset includes financial metrics (revenue, spending, net balance) and performance metrics (goals, wins, losses, league positions) for the top 10 teams from 15 European leagues. The scraped data will form the foundation for further analysis in the project.
           
**2. [Notebook_2_Data_Understanding](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks/Notebook_2_Data_Understanding.ipynb):** This notebook is dedicated to exploring the collected data to gain insights into its structure and content. It provides an overview of the dataset's features, highlighting numerical and categorical columns, identifying missing values, and detecting duplicates. The notebook sets the stage for further data cleaning and analysis by offering a comprehensive summary of the dataset's current state.
           
**3. [Notebook_3_Data_Cleaning_and_Preprocessing](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks/Notebook_3_Data_Cleaning_and_Preprocessing.ipynb):** This notebook focuses on cleaning and preprocessing the collected data. It includes steps such as handling missing values, transforming categorical variables, and detecting outliers. The goal is to prepare the dataset for analysis by ensuring it is free of inconsistencies, properly formatted, and ready for further processing in the next stages of the project.
           
**4. [Notebook_4_Data_Validation](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks/Notebook_4_Data_Validation.ipynb):** In this notebook, the cleaned and preprocessed data is validated for accuracy and consistency. The process involves cross-checking for errors, verifying that all necessary transformations were correctly applied, and ensuring that the dataset is suitable for further exploratory data analysis.
           
**5. [Notebook_5_Exploratory_Data_Analysis](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/02%20-%20Notebooks/Notebook_5_Exploratory_Data_Analysis.ipynb):** This notebook conducts an Exploratory Data Analysis (EDA) to examine financial efficiency and performance metrics in European football leagues. The analysis focuses on how financial spending correlates with team performance, identifying patterns over time, and comparing financial and performance metrics across different leagues. The notebook uses visualizations and descriptive statistics to uncover key insights regarding financial dynamics in European football.

+ **Revenue & Spending Analysis:** Identification of high-revenue leagues like Italy, England, and Spain, each averaging over €30 million.

+ **Performance Metrics Analysis:** Examined how spending affects goals, wins, and losses, with visualizations showing varying degrees of correlation across leagues.

### [Data](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/03%20-%20Data)

This folder contains the data used for analyzing financial and performance metrics across European football leagues, including the raw collected data and the final cleaned dataset after preprocessing. It includes the following CSV files:

+ **[first_data](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/03%20-%20Data/first_data.csv):** This file contains the raw data obtained through web scraping from Transfermarkt, capturing financial and performance metrics for 4,342 entries across 15 European football leagues. It includes key columns such as league, team, season, revenue, spent, net, goals for, wins, losses, and position. This dataset represents the initial unprocessed data used for analysis, featuring both financial and performance indicators that will later be cleaned and transformed.
           
+ **[clean_data](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/03%20-%20Data/clean_data.csv):** This file holds the final dataset after completing the cleaning, preprocessing, and validation steps. The data includes 32 columns, with key transformations like log transformations for financial metrics (e.g., log_revenue, log_spent), and performance metrics such as sqrt_goals_for and net_cube_root. New features like winsorized 5-season net and log 5-season relative have been added, providing a refined and structured dataset ready for exploratory analysis.

### [Dashboard](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/04%20-%20Dashboard)

This folder contains the interactive dashboard for analyzing financial and performance metrics in European football leagues, built with Streamlit. It includes the following files:

+ **[app](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/04%20-%20Dashboard/app.py):** This file contains the code for generating the interactive dashboard. It uses the Streamlit framework to visualize the cleaned data and allow users to explore financial and performance metrics of European football leagues. Running this file will produce the dashboard interface, enabling dynamic analysis of the data.
         
+ **[requirements](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/04%20-%20Dashboard/requirements.txt):** This file lists the dependencies required to run your project, including important libraries such as: numpy, pandas, streamlit, streamlit-option-menu, scikit-learn and matplotlib.
           
+ **[clean_data2](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/02%20-%20Exploratory-Data-Analysis-EDA-Projects/01%20-%20Financial%20Efficiency%20and%20Performance%20Metrics%20Analysis%20of%20European%20Football%20Leagues/04%20-%20Dashboard/clean_data2.csv):** This file represents the final cleaned dataset after completing the data cleaning, preprocessing, and validation stages. It is used in the dashboard to present the analysis of financial and performance metrics for European football teams, showcasing the results through interactive visualizations.  

### Presentation

This folder contains the final project presentation, summarizing the objectives, methodology, and key findings from the analysis of financial and performance metrics of football teams across European leagues. It includes the following presentation file:

         + [Final Project Presentation](): This file contains the presentation for your final project titled "Financial Efficiency and Performance Metrics Analysis of European Football Leagues". The presentation covers the project's objectives, methodology, and key findings, highlighting the relationship between financial spending and team performance across various European football leagues. It includes data features such as revenue, spending, net balance, wins, and goals, as well as insights into how financial efficiency impacts team success. The presentation also emphasizes the importance of strategic financial management for long-term stability and success in football.

## 📊 Key Insights & Findings

Revenue and Spending Insights: High-revenue leagues like Italy, England, and Spain dominate in revenue generation, supported by broadcasting deals and sponsorships. England’s Premier League exhibits the highest spending but also reports the most significant deficits, highlighting potential financial risks.

Financial Sustainability: Leagues like Portugal and Netherlands demonstrate sustainable financial strategies, managing moderate budgets effectively while maintaining competitive performance.

Spending and Performance Correlation: Spending correlates positively with team performance metrics, particularly in top leagues. However, efficiency varies significantly across leagues, with some achieving competitive success through strategic spending rather than high expenditures.

Long-term Trends: Over time, financial powerhouses continue to dominate, but smaller leagues are increasingly focusing on sustainable growth and player development, balancing financial investments with long-term stability.

## 🔑 Conclusion

This project reveals how data science provides valuable insights into financial dynamics and performance metrics within European football. The analysis underscores the need for disciplined financial strategies to secure long-term stability and enhance team competitiveness across leagues.

Whether you’re a student, an analyst, or a stakeholder in the sports industry, this project demonstrates the potential of data-driven insights to shape strategies, drive financial efficiency, and foster success in European football leagues.
