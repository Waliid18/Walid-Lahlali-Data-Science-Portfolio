# Financial Efficiency and Performance Metrics Analysis of European Football Leagues

## 📌 Project Overview

This project examines financial efficiency and performance metrics of football teams across 15 European leagues, providing a comprehensive Exploratory Data Analysis (EDA). It explores how financial spending impacts team performance, identifies patterns over time, and offers valuable insights through an interactive dashboard. This analysis addresses key questions surrounding financial efficiency, strategic spending, and performance dynamics across different leagues.

## 📂 Repository Structure

This project is organized into five main folders: Proposal, Notebooks, Data, Dashboard, and Presentation. The structure is as follows:

#### Proposal

Final Capstone Project Proposal: This document outlines the project objectives, methodology, and key deliverables. The goal is an in-depth EDA of financial and performance metrics across 15 European leagues, analyzing the relationship between financial investment and team performance using financial data (e.g., revenue, spending) and performance indicators (e.g., goals, wins).

#### Notebooks

Each notebook documents a stage in the analytical process:

Notebook_1_Data_Collection: Data was collected through web scraping from Transfermarkt, targeting metrics such as revenue, spending, and performance for the top teams across leagues.

Notebook_2_Data_Understanding: This notebook provides a comprehensive exploration of the dataset, including a summary of categorical and numerical features, identification of missing values, and an initial correlation analysis.

Notebook_3_Data_Cleaning_and_Preprocessing: Here, the dataset was cleaned, transformed, and prepared for analysis. Steps included handling missing values, encoding categorical data, scaling features, and treating outliers to ensure data integrity.

Notebook_4_Data_Validation: This notebook validates the accuracy and consistency of the cleaned data, verifying that preprocessing steps have been applied correctly.

Notebook_5_Exploratory_Data_Analysis: This notebook conducts a thorough EDA. Key analyses include:

Revenue & Spending Analysis: Identification of high-revenue leagues like Italy, England, and Spain, each averaging over €30 million.
Performance Metrics Analysis: Examined how spending affects goals, wins, and losses, with visualizations showing varying degrees of correlation across leagues.

#### Data

Contains both raw and processed datasets used throughout the project:

first_data.csv: Raw data scraped from Transfermarkt, containing financial and performance metrics for teams in European leagues.
clean_data.csv: The cleaned and processed dataset, featuring transformations like log-scaling of revenue and spending, enabling a more refined analysis.

#### Dashboard

An interactive Streamlit dashboard provides an intuitive exploration of the data:

app.py: The code for generating the dashboard, which visualizes financial and performance metrics, allowing users to filter data by league and team.
requirements.txt: Dependencies for running the project, including essential libraries like numpy, pandas, streamlit, and matplotlib.
clean_data2.csv: Used within the dashboard, this file presents cleaned data to support real-time analysis.

#### Presentation

Final Project Presentation: A PDF summarizing project objectives, methodology, and key insights, showcasing the relationship between financial efficiency and team performance across leagues.

## 📊 Key Insights & Findings

Revenue and Spending Insights: High-revenue leagues like Italy, England, and Spain dominate in revenue generation, supported by broadcasting deals and sponsorships. England’s Premier League exhibits the highest spending but also reports the most significant deficits, highlighting potential financial risks.

Financial Sustainability: Leagues like Portugal and Netherlands demonstrate sustainable financial strategies, managing moderate budgets effectively while maintaining competitive performance.

Spending and Performance Correlation: Spending correlates positively with team performance metrics, particularly in top leagues. However, efficiency varies significantly across leagues, with some achieving competitive success through strategic spending rather than high expenditures.

Long-term Trends: Over time, financial powerhouses continue to dominate, but smaller leagues are increasingly focusing on sustainable growth and player development, balancing financial investments with long-term stability.

## 🔑 Conclusion

This project reveals how data science provides valuable insights into financial dynamics and performance metrics within European football. The analysis underscores the need for disciplined financial strategies to secure long-term stability and enhance team competitiveness across leagues.

Whether you’re a student, an analyst, or a stakeholder in the sports industry, this project demonstrates the potential of data-driven insights to shape strategies, drive financial efficiency, and foster success in European football leagues.
