# Financial Efficiency and Performance Metrics Analysis of European Football Leagues

## Overview

This project is the final project for the Data Science Bootcamp at Concordia University, prepared by Mr. Walid Lahlali under the supervision of Mr. Joseph Peart. The project aims to analyze the financial efficiency and performance metrics of European football leagues, focusing on 15 major leagues, including England, Spain, Italy, Germany, France, Portugal, Netherlands, Türkiye, Belgium, Russia, Greece, Austria, Ukraine, Denmark, and Switzerland.

The analysis is split across five notebooks and an interactive dashboard, providing insights into how financial spending correlates with team performance, identifying trends over time, and comparing different leagues based on various metrics.

## Repository Structure

The repository is organized into the following folders:

+ [Notebooks](https://github.com/Waliid18/Final-Project/tree/main/Notebooks): Contains the Jupyter notebooks used in the analysis.
  + [Notebook_1_Data_Collection.ipynb](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_1_Data_Collection.ipynb)
  + [Notebook_2_Data_Understanding.ipynb](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_2_Data_Understanding.ipynb) 
  + [Notebook_3_Data_Cleaning_and_Preprocessing.ipynb](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_3_Data_Cleaning_and_Preprocessing.ipynb)
  + [Notebook_4_Data_Validation.ipynb](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_4_Data_Validation.ipynb)
  + [Notebook_5_Exploratory_Data_Analysis.ipynb](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_5_Exploratory_Data_Analysis.ipynb)
+ [Data](https://github.com/Waliid18/Final-Project/tree/main/Data): Includes the dataset used in the analysis.
+ [Dashboard](https://github.com/Waliid18/Final-Project/blob/main/Dashboard/app.py): Contains the files related to the interactive dashboard deployed using Streamlit. [Dashboard's link](https://de79-38-133-46-148.ngrok-free.app)
+ [presentation](https://github.com/Waliid18/Final-Project/blob/main/Presentation/Final%20Project%20Presentation.pdf): Contains the final presentation summarizing the project.
+ [Proposal](https://github.com/Waliid18/Final-Project/blob/main/Proposal/Final%20Capstone%20Project%20Proposal.pdf): Includes the initial project proposal outlining the objectives and methodology.

## Notebooks Summary

### 1. Notebook 1: [Data Collection](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_1_Data_Collection.ipynb)
This notebook focuses on gathering data from the [Transfermarkt](https://www.transfermarkt.us/) website, covering financial and performance metrics of football teams from the selected European leagues. The data includes key columns such as **league**, **team**, **season**, **revenue**, **spent**, **net, goals_for**, **goals_against**, **wins**, **ties**, and **losses**.

### 2. Notebook 2: [Data Understanding](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_2_Data_Understanding.ipynb)
In this notebook, the structure and content of the dataset are examined to gain a better understanding. This includes visualizing distributions, identifying potential issues such as missing values, and exploring initial correlations between financial and performance metrics.

### 3. Notebook 3: [Data Cleaning and Preprocessing](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_3_Data_Cleaning_and_Preprocessing.ipynb)
The third notebook focuses on cleaning and preprocessing the data. Key steps include handling missing data, converting categorical variables into numerical formats, and engineering new features to enhance the analysis. Outliers are also detected and addressed to ensure the integrity of the data.

### 4. Notebook 4: [Data Validation](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_4_Data_Validation.ipynb)
In this notebook, the cleaned and processed data is validated to ensure it meets the required standards for analysis. This includes verifying the consistency of data types, ensuring that all necessary transformations have been applied, and confirming the absence of any remaining outliers or missing values.

### 5. Notebook 5: [Exploratory Data Analysis (EDA)](https://github.com/Waliid18/Final-Project/blob/main/Notebooks/Notebook_5_Exploratory_Data_Analysis.ipynb)
The final notebook is dedicated to an in-depth exploratory data analysis, where various visualizations and statistical techniques are applied to understand the financial and performance dynamics of European football leagues. Below are some of the key findings:

#### 5.1 Revenue Analysis by League
+ **Top Revenue Leagues:** Italy, England, and Spain are the leading leagues in terms of average revenue, each generating over €30 million on average. This reflects their strong financial position, supported by lucrative broadcasting deals, sponsorships, and commercial activities. These leagues are financial powerhouses, enabling significant investments in player acquisitions, infrastructure, and other resources that contribute to their competitive advantage.
+ **Moderate Revenue Leagues:** France and Germany also show strong revenue figures, though slightly lower than the top three. These leagues still generate significant income, supporting their status as major players in European football.
+ **Lower Revenue Leagues:** Greece, Switzerland, Austria, and Turkey are at the lower end of the revenue spectrum, with average revenues below €5 million. This suggests that teams in these leagues may have more limited financial resources, potentially affecting their ability to compete at the highest levels.

#### 5.2 Spending Analysis by League
+ **Top Spending Leagues:** England leads by a significant margin, with an average spending of over €70 million, followed by Italy and Spain with average spending around €48 million and €42 million, respectively. This reflects the intense competition and high financial stakes in these leagues, where clubs invest heavily in acquiring top talent and maintaining competitive squads.
+ **Moderate Spending Leagues:** Germany and France also show substantial spending, with averages around €30 million and €25 million, respectively. These leagues balance their financial capabilities with their competitive ambitions.
+ **Lower Spending Leagues:** Leagues like Greece, Switzerland, and Austria have much lower spending figures, often below €10 million. These leagues operate with more modest budgets, focusing on nurturing local talent and maintaining financial sustainability.
#### 5.3 Net Balance Analysis
+ **High Deficit Leagues:** The Premier League (England) consistently shows a high negative net balance, indicating that spending significantly outpaces revenue. This trend highlights the financial risks involved, where clubs prioritize short-term competitive success over long-term financial stability.
+ **Stable Net Balance Leagues:** Spain’s relatively stable net balance suggests a cautious financial approach, aiming to balance competitive performance with financial prudence.
+ **Sustainable Spending Leagues:** Portugal and the Netherlands demonstrate a more sustainable approach, with net balances that suggest careful financial management and a focus on long-term success rather than immediate expenditure.
#### 5.4 Correlation Between Spending and Performance
The analysis reveals a positive correlation between spending and on-field performance across the leagues, particularly in top-tier leagues like England, Spain, and Italy. However, the correlation is not absolute, indicating that financial management and strategic spending are equally important. For instance, teams in Portugal and the Netherlands achieve competitive success with more modest financial resources, emphasizing the importance of efficiency.

#### 5.5 League-Wise Performance Metrics
+ **Goals and Wins:** The analysis of goals scored and matches won across leagues indicates that while spending correlates with performance, tactical efficiency and player development also play crucial roles. For example, leagues like Italy and Spain show a balance between financial expenditure and performance, while others like Greece and Switzerland highlight the challenges of competing with limited resources.
+ **Long-Term Trends:** The analysis also explores long-term trends, revealing that while financial powerhouses continue to dominate, smaller leagues are increasingly focusing on sustainable growth and player development.
#### Conclusion
This project highlights the intricate balance between financial management and on-field success in European football leagues. While top leagues like England, Spain, and Italy dominate in both revenue generation and spending, this financial power does not necessarily guarantee sustainability. The consistent trend of spending outpacing revenue across these leagues poses significant financial risks, as evidenced by the increasingly negative net balances, particularly in the Premier League.

Moreover, the correlation between spending and performance, while positive, is not absolute—indicating that strategic financial management is as crucial as the amount spent. Teams that manage their finances prudently, such as those in Portugal and the Netherlands, demonstrate that sustainable success is possible even with more modest resources.

In summary, the project underscores the need for European football leagues to adopt disciplined financial strategies to ensure long-term stability and success. As leagues continue to grow financially, the challenge will be to translate this growth into sustainable operations that not only enhance competitive performance but also secure the financial health of the clubs.
