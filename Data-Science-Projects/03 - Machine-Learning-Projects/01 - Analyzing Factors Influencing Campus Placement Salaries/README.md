# README: Analyzing Factors Influencing Campus Placement Salaries
## Project Overview
This project aims to analyze the various factors that influence the salaries offered to students during campus placements. Using a dataset containing students' academic records, demographic details, and placement status, the objective is to build a predictive model that can estimate the salary a student might receive based on these factors.

## Dataset Description
The dataset used in this project includes the following columns:

+ **sl_no:** Serial Number to identify each candidate.
+ **gender:** Gender of the candidate (M/F).
+ **ssc_p:** Secondary Education percentage (10th Grade).
+ **ssc_b:** Board of Education for Secondary School (Central/Other).
+ **hsc_p:** Higher Secondary Education percentage (12th Grade).
+ **hsc_b:** Board of Education for Higher Secondary School (Central/Other).
+ **hsc_s:** Specialization in Higher Secondary Education.
+ **degree_p:** Degree percentage.
+ **degree_t:** Type of degree obtained (field of study).
+ **workex:** Work experience (Yes/No).
+ **etest_p:** Employability test percentage (conducted by the college).
+ **specialisation:** Specialization in MBA (Marketing/Finance, Marketing/HR).
+ **mba_p:** MBA percentage.
+ **status:** Placement status of the candidate (Placed/Not Placed).
+ **salary:** Salary offered by the company to the candidate.
  
## Project Workflow

## Data Preprocessing:

+ **Handling Missing Data:** The salary column had missing values that were filled with 0 to represent students who did not receive a placement offer.
+ **Encoding Categorical Variables:** Categorical columns were encoded using LabelEncoder to convert them into numerical format suitable for machine learning models.
+ **Feature Scaling:** Numeric features were standardized using StandardScaler to ensure all features contributed equally to the model.
  
## Exploratory Data Analysis (EDA):

+ **Distribution Analysis:** The distributions of numeric columns were visualized to understand the spread and central tendencies of the data.
+ **Correlation Analysis:** A heatmap was generated to visualize the correlations between different variables. It highlighted that while academic percentages and test scores are important, they do not alone determine salary outcomes.
+ **Pair Plot:** Pair plots were created to examine the relationships between various features, showing limited correlations between academic scores and salary.
  
## Model Development:

Multiple machine learning models were trained and evaluated, including:
+ **Linear Regression**
+ **Decision Tree Regressor**
+ **Random Forest Regressor**
  
The models were evaluated based on their Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

## Model Evaluation:

**Linear Regression:**

+ **R² Score:** 0.8560
+ **RMSE:** 57060.1436
+ **MAE:** 41062.6824
  
**Decision Tree Regressor:**

+ **R² Score:** 0.8109
+ **RMSE:** 65378.2699
+ **MAE:** 37772.7273

**Random Forest Regressor (Best Performing Model):**

+ **R² Score:** 0.9398
+ **RMSE:** 38300.2659
+ **MAE:** 22184.5455
  
The Random Forest Regressor was selected as the best-performing model due to its high R² score and low MAE and RMSE.

## Model Testing on New Data:

The trained Random Forest model was used to predict salaries for new data. The predicted salaries were consistent and aligned with expectations, demonstrating the model's effectiveness.

## Key Results

The Random Forest Regressor was the most effective model, with an R² score of 0.9398 on the test set.
The model was able to predict salaries with reasonable accuracy, suggesting that while academic and test scores are important, they are part of a broader set of factors influencing campus placement outcomes.

## Conclusion

This project demonstrates the potential of machine learning to predict campus placement salaries based on a combination of academic performance, test scores, and demographic data. The Random Forest model proved to be the most robust, offering valuable insights into the factors that contribute to salary outcomes. Future work could involve incorporating additional features or refining the model further to improve predictive accuracy.

