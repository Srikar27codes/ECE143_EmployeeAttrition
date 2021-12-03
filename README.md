# ECE143 Group 17 - IBM Employee Attrition Analysis
The project is about performing EDAs and deep analysis on the IBM Employee Attrition dataset, and conclude on reasonable factors that may cause employee attrition at IBM.

## Dataset
The [IBM employee dataset](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset) contains ~1500 employees’ information in more than thirty features. Some features like Age, salary, marital status, gender, and attrition are noteworthy.

### Setup:
Install the packages using conda to setup environment with env.yml file
All the modules are located in src folder

### Scripts and Notebook
-  Python files
    -   To get the plots shown in the presentation: ./run.py
    - Preprocessing Data: ./src/preprocess.py
    - T-test analysis: ./src/ttest_analysis.py
    - Visualization: ./src/visualization.py
- Python notebook
    - All the visualizations and experiments done can be run using ./visualization/Visualization.ipynb

### Repo structure
```
│   .gitignore
│   env.yml
│   Group17_ECE143_presentation.pdf
│   README.md
│   run.py
│
├───data
│   ├───preprocessed
│   │       Categorical_Cols.csv
│   │       Employee_Attrited.csv
│   │       Employee_Remained.csv
│   │       HR_Employee_Attrition.csv
│   │       Numerical_Cols.csv
│   │
│   ├───raw
│   │       HR_Employee_Attrition.csv
│   │
│   └───ttest
│           ttest_outcome.csv
│
├───notebook
│       Visualization.ipynb
│
├───plot
│       Age_distribution_to_attrition.png
│       All_people_overtime_to_attrition.png
│       DistanceFromHome_distribution_to_attrition.png
│       Divorced_people_overtime_to_attrition.png
│       Married_people_overtime_to_attrition.png
│       MonthlyIncome_distribution_to_attrition.png
│       monthlyincome_to_totalworkingyears.png
│       Single_people_overtime_to_attrition.png
│       {}_age_bracket_to_attrition.png
│
└───src
    │   preprocess.py
    │   ttest_analysis.py
    │   visualization.py
```

### Preprocessing
Classify all comlunms into 3 groups:
- Key column: Attrition (Yes/No)
- Numerical columns: Age, Monthly Income, Distance from home, etc.
- Categorical columns: Overtime, Job Level, Employee Satisfaction, etc.

## Methodology
- Setup hypotheses
- Test the hypotheses by visualizing the graphs
- Confirm what we found using statistical tests

