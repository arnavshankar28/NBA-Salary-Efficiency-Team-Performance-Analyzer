# NBA Salary Efficiency and Team Performance Analyzer

## Project Overview

The NBA Salary Efficiency Analyzer is a sports analytics project that investigates how efficiently NBA teams spend their payroll relative to their on-court performance.

The goal is to combine team payroll, salary cap information, traditional statistics, and advanced statistics into one master dataset and use data analytics and machine learning to answer questions about team efficiency.

This project combines my interests in artificial intelligence, finance, sports analytics, data analytics, and data science.


## Research Question

**How efficiently do NBA franchises convert payroll expenditures into regular-season performance, and which organizations maximize competitive outcomes relative to financial investment?**

---

## Objectives

- Merge multiple NBA datasets into one master dataset
- Clean and organize real-world data
- Perform exploratory data analysis (EDA)
- Create professional visualizations
- Build machine learning models to predict team success
- Develop an interactive dashboard using Streamlit
- Present actionable insights about NBA salary efficiency and team performance

---

## Datasets Used

This project combines multiple publicly available NBA datasets, including:

- Team payroll
- Salary cap information
- Team statistics
- Advanced team statistics

These datasets are merged into a single master dataset for analysis.

---

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- GitHub

---

## Current Features

- Data cleaning and preprocessing
- Combined master dataset
- Exploratory data analysis
- Salary efficiency metrics
- Team performance comparisons
- Machine learning prediction models
- Interactive dashboard (in progress)

---

## Project Structure

```
NBA-Salary-Efficiency-Analyzer
│
├── data/
  NBA_team_payroll_2026.csv
  NBA_team_salarycap_2026.csv
  NBA_team_stats.csv
  NBA_team_stats2.csv
  NBA_Master_Dataset_2026.csv
  NBA_Master_Dataset_V2_2026.csv
  NBA_Teams_ShootingStats_2025-26.csv
  NBA_Salaries.csv
├── notebooks/
  nba_salaries.ipynb
  NBA_Master_Dataset_2026.ipynb
  NBA_Salary_Efficiency_Table.ipynb
  NBA_team_payroll_2026.ipynb
  NBA_team_salarycap_2026.ipynb
  NBA_Teams Notebook.ipynb
  NBA_Teams Notebook2.ipynb
  NBA_Master_Dataset_V2_2026.ipynb
  NBA_PRediciton_Model_V2.ipynb
├── dashboard/
├── charts/
  NBA Team Payroll by Team (2026).png
  NBA Team Total Points (2026).png
  NBA_teams_losses_2026.png
  NBA_teams_PPG.png
  NBA_teams_wins_2026.png
  Cost Per Win by NBA Team.png
  NBA Team Payroll vs Wins (2025-2026).png
  Top 10 Highest NBA Team Payrolls.png
  NBA_Master_Dataset_HeatMap_ImportantFeatures.png
└── README.md
```

---

## Prediction Model
A Random Forest Regressor was developed to predict NBA team regular season wins using advanced team statistics, payroll data, and roster metrics. The model was optimized using GridSearchCV and evaluated with 5-fold repeated cross-validation, achieving an average MAE of 4.98 wins, RMSE of 5.75 wins, and R² of 0.688, explaining approximately 69% of the variation in team wins.

## Key Questions

Some questions this project explores include:

- Does spending more money lead to more wins?
- Which teams outperform their payroll?
- Which teams underperform despite large payrolls?
- What statistics are most closely related to winning?
- Can machine learning predict team success using team statistics?

---

## Skills Demonstrated

This project demonstrates experience with:

- Data cleaning
- Data visualization
- Exploratory data analysis
- Feature selection
- Machine learning
- Decision trees
- Model evaluation
- Sports analytics
- GitHub version control

---

## Future Improvements

Future versions of this project will include:

- Additional machine learning models
- Player-level salary efficiency analysis
- Multi-season comparisons
- Advanced dashboard features
- Interactive filtering
- Predictive salary efficiency metrics

---

## About Me

I am a rising junior at The Peddie School with interests in artificial intelligence, finance, data analytics, and sports analytics.

This project is part of my Summer 2026 independent AI and data analytics research project, where I am developing practical machine learning and data science skills through real-world projects.

---

## License

This project is intended for educational and portfolio purposes.
