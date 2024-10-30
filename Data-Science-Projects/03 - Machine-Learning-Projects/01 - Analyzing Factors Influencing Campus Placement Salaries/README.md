# Analyzing Factors Influencing Campus Placement Salaries

## 📌 Project Overview

The transition from academia to a professional career often hinges on campus placements, where salary offers play a critical role. This project delves into the intricate factors that influence these placement salaries, analyzing academic records, demographic details, and additional qualifications to build a predictive model that provides insights into potential salary outcomes. The Random Forest Regressor was selected as the best model for its accuracy and interpretability, shedding light on the multifaceted elements that impact a candidate's salary potential.

## 📂 Project Structure

The project is meticulously organized for seamless exploration:

+ **[Notebooks](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/01%20-%20Notebooks):** Contains Jupyter notebook "[Analyzing Factors Influencing Campus Placement Salaries](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/01%20-%20Notebooks/Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries.ipynb)" documenting each step of the analysis, from data exploration to model evaluation.

+ **[Data](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/02%20-%20Data):** Houses the primary [dataset](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/02%20-%20Data/Placement_Data_Full_Class_1.csv) used throughout the project.

+ **[Models](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/tree/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/03%20-%20Models):** Contains the final deployment-ready file of the [best-performing model (Random Forest Regressor)](https://github.com/Waliid18/Walid-Lahlali-Data-Science-Portfolio/blob/main/Data-Science-Projects/03%20-%20Machine-Learning-Projects/01%20-%20Analyzing%20Factors%20Influencing%20Campus%20Placement%20Salaries/03%20-%20Models/random_forest_model.pkl), ready for real-world predictions.

## 📊 Dataset Description

The dataset is a comprehensive snapshot of students’ academic performance, work experience, and other critical characteristics. It includes **215** observations with features that capture the candidate’s educational and demographic profile:

+ **Academic Scores:** Represented by `ssc_p` (Secondary), `hsc_p` (Higher Secondary), `degree_p` (Degree), and `mba_p` (MBA) percentages.
  
+ **Demographics:** Features such as `gender`, `ssc_b` (Secondary board), `hsc_b` (Higher Secondary board), `hsc_s` (Higher Secondary specialization), and `degree_t` (Degree type).
  
+ **Experience & Specialization:** Work experience (`workex`), MBA specialization (`specialisation`).
  
+ **Outcome Variables:** `status` (Placement Status) and `salary` (offered salary for placed candidates).
  
The dataset provides a nuanced view of candidates’ profiles, highlighting key characteristics that influence placement success and salary outcomes.

## 🔍 Exploratory Data Analysis (EDA)

EDA provides essential insights into the data's structure and relationships, enabling better model performance and interpretability.

Categorical Features Analysis
Gender Distribution: Male candidates form a larger portion of the dataset.
Academic Backgrounds: Most students completed secondary education from the "Central" board and specialized in Commerce or Science fields in Higher Secondary.
MBA Specialization: Marketing & Finance is the most common MBA specialization among placed students, followed by Marketing & HR.
Work Experience: A significant portion of students lacks work experience, though those with experience generally received higher placement offers.
Numerical Features Analysis
Salary Distribution: Highly skewed, with most salaries around the lower end, reflecting high placement variation. The average salary stands at approximately 198,702.
Academic Performance: Most scores cluster around 60-70%, with a few high-achievers in employability tests and MBA scores.
Correlation Analysis: Limited correlations with salary, indicating that multiple factors, including but not limited to academic performance, contribute to salary outcomes.
Visualization Insights
Correlation Matrix: Showcases a low correlation between salary and other features, suggesting a mix of factors influences outcomes.
Pair Plots: Confirms limited associations between academic scores and salary, underlining the importance of additional features like experience.

## 🚀 Model Development & Evaluation

Three regression models were developed, evaluated, and compared based on performance metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

1. Linear Regression
MAE: ~41,062
RMSE: ~57,060
R² Score: 0.856
Performance: Offers moderate predictive power, limited by linear assumptions.
2. Decision Tree Regressor
MAE: ~37,772
RMSE: ~65,378
R² Score: 0.811
Performance: Captures non-linear patterns but overfits on test data, reducing generalizability.
3. Random Forest Regressor (Best Model)
MAE: ~22,185
RMSE: ~38,300
R² Score: 0.940
Performance: Excels in accuracy and variance capture, emerging as the most reliable model for salary predictions. Random Forest balances the dataset’s complexity, capturing a mix of linear and non-linear relationships.
Cross-Validation Results
The Random Forest Regressor maintained consistent accuracy across multiple data folds, confirming its robustness and suitability for production deployment.

## 📈 Key Insights & Findings

Multi-Factor Influence on Salaries: While academic performance is significant, factors like employability scores and MBA specialization also contribute meaningfully. The Random Forest Regressor's strength lies in integrating these elements to deliver precise salary predictions.
Model Selection: The Random Forest Regressor demonstrated exceptional predictive performance, highlighting the value of ensemble methods for complex data relationships.
Future Scope: Additional demographic features or advanced tuning may improve prediction accuracy, offering even greater clarity into the dynamics of campus placements.

## 🔑 Conclusion

This project exemplifies how data science can provide insights into real-world outcomes, such as campus placements, by analyzing multiple factors. The Random Forest Regressor has proven highly effective, demonstrating that predicting campus placement salaries requires a multi-dimensional approach. Future advancements could include refining features or experimenting with alternative ensemble techniques to capture deeper patterns.

Whether you're a student preparing for placements, an institution shaping recruitment strategies, or a recruiter targeting the best talent, these insights empower informed decision-making in campus hiring landscapes.
