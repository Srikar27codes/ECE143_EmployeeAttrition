# preprocess.py
# load raw dataset and preprocess it several subsets for further analysis

import pandas as pd
def preprocess_df(rawpath:str='data/raw/HR_Employee_Attrition.csv',outpath:str='data/preprocessed/'):
    '''
    Take the raw dataset and preprocess it into several datasets for future gender_analysis

    Param:
        rawpath: path to raw dataset
        outpath: path to output datasets
    Return:
        None
    '''
    df_raw = pd.read_csv(rawpath)

    # Drop invalid columns
    df_preprocess = df_raw.drop(columns=["EmployeeNumber","EmployeeCount", "Over18", "StandardHours"])
    df_preprocess = df_preprocess.replace({
        "Attrition": {
            'Yes':1,
            'No': 0
            },
        "BusinessTravel": {
            "Travel_Rarely":0,
            "Travel_Frequently":1
        },
        "OverTime": {
            'Yes':1,
            'No':0
        },
        "JobInvolvement": {
            1 : "Low",
            2 : "Medium",
            3 : "High",
            4 : "Very High"
        },
        "JobSatisfaction": {\
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
    df_preprocess.to_csv(outpath+'HR_Employee_Attrition.csv')

    # Classify columns into the numerical group and categorical group
    df_numerical = df_preprocess[['Attrition', 'Age','DistanceFromHome', 'HourlyRate', 'DailyRate', 'MonthlyRate', 'MonthlyIncome', 'PercentSalaryHike',
        'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion','YearsWithCurrManager','NumCompaniesWorked','TrainingTimesLastYear']]
    df_categorical = df_preprocess[['Attrition', 'Gender', 'OverTime', 'MaritalStatus', 'EnvironmentSatisfaction', 'JobSatisfaction','RelationshipSatisfaction',
        'WorkLifeBalance', 'JobInvolvement', 'PerformanceRating','BusinessTravel','Education','EducationField','JobLevel','JobRole','Department','StockOptionLevel']]
    df_numerical.to_csv(outpath+'Numerical_Cols.csv')
    df_categorical.to_csv(outpath+'Categorical_Cols.csv')

    # Classify columns into the attrited group and those still stayed in the company
    df_attrited = df_preprocess.loc[df_preprocess['Attrition']==1].reset_index(drop=True)
    df_remained = df_preprocess.loc[df_preprocess['Attrition']==0].reset_index(drop=True)
    df_attrited.to_csv(outpath+'Employee_Attrited.csv')
    df_remained.to_csv(outpath+'Employee_Remained.csv')
