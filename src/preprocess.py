# preprocess.py
# load raw dataset and preprocess it several subsets for further analysis

import numpy as np
import pandas as pd

rawDataPath, preprocessDataPath = 'data/raw/', 'data/preprocessed/'
df_raw = pd.read_csv('data/raw/HR_Employee_Attrition.csv')
df_raw.head(5)
df_raw.info()

# Drop invalid columns 
df_preprocess = df_raw.drop(columns=["EmployeeNumber","EmployeeCount", "Over18", "StandardHours"])
print(df_preprocess.dtypes)
df_preprocess = df_preprocess.replace({
    "Attrition": {
        'Yes':1,
        'No': 0
        },
    "BusinessTravel": {
        "Travel_Rarely":0,
        "Travel_Frequently":1
    },
    "Overtime": {
        'Yes':1,
        'No':0
    },
    'Education': {
        1 : "Below College",
        2 : "College",
        3 : "Bachelors", 
        4 : "Masters", 
        5 : "PhD"
    },
    "JobInvolvement": {
        1 : "Low",
        2 : "Medium",
        3 : "High",
        4 : "Very High"
    },
    "JobSatisfaction": {
        1 : "Low",
        2 : "Medium",
        3 : "High",
        4 : "Very High"
    },
    "PerformanceRating": {
        1 : "Low",
        2 : "Medium",
        3 : "High",
        4 : "Very High"
    }
})
df_preprocess.to_csv(preprocessDataPath+'HR_Employee_Attrition.csv')

# Classify columns into the numerical group and categorical group
df_numerical = df_preprocess[['Attrition', 'Age','DistanceFromHome', 'HourlyRate', 'DailyRate', 'MonthlyRate', 'MonthlyIncome', 'PercentSalaryHike', 
    'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion','YearsWithCurrManager','NumCompaniesWorked','TrainingTimesLastYear']]
df_categorical = df_preprocess[['Attrition', 'Gender', 'OverTime', 'MaritalStatus', 'EnvironmentSatisfaction', 'JobSatisfaction','RelationshipSatisfaction', 
    'WorkLifeBalance', 'JobInvolvement', 'PerformanceRating','BusinessTravel','Education','EducationField','JobLevel','JobRole','Department','StockOptionLevel']]
df_numerical.to_csv(preprocessDataPath+'Numerical_Cols.csv')
df_categorical.to_csv(preprocessDataPath+'Categorical_Cols.csv')

# Classify columns into the attrited group and those still stayed in the company
df_attrited = df_preprocess.loc[df_preprocess['Attrition']==1].reset_index(drop=True)
df_remained = df_preprocess.loc[df_preprocess['Attrition']==0].reset_index(drop=True)
df_attrited.to_csv(preprocessDataPath+'Employee_Attrited.csv')
df_remained.to_csv(preprocessDataPath+'Employee_Remained.csv')
