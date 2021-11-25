# categorical_analysis.py
# simple analysis on categorical columns

import numpy as np
import pandas as pd

# Data extraction
df_categorical = pd.read_csv('data/preprossed/Categorical_Cols.csv')

# 1. Attrition results on Gender
# a) Percentage difference on Male and Female
df_categorical['Gender'].value_counts().plot.pie(figsize=(7, 5), colors = ['sandybrown','cornflowerblue'], autopct='%.2f%%', rot=0)
# b) Attrition comparison on Male and Female
df_categorical[['Gender', 'Attrition']].value_counts().unstack().plot.bar(figsize=(7, 5), xlabel='Gender', ylabel='Counts',color = ['sandybrown','cornflowerblue'], rot=0)

# 2. Attrition results on JobSatisfaction
# a) Percentage difference on 4 degrees of JobSatisfaction
df_categorical['JobSatisfaction'].value_counts().plot.pie(figsize=(7, 5), autopct='%.2f%%', rot=0)
# b) Attrition comparison on JobSatisfaction
# The table shows percentages on different job satisfaction based on Attrition Yes or No respectively
attr_jobSatisfaction = df_categorical[['Attrition', 'JobSatisfaction']].value_counts().unstack()
percentage_attr_jobSatis = attr_jobSatisfaction.T/attr_jobSatisfaction.apply(sum, axis=1)*100
percentage_attr_jobSatis.plot.bar(figsize=(7, 5), xlabel='Job Satisfaction', ylabel='Percentage_attrition',rot=0)
# c) normalization
# this gives a ratio of the number of people who left with the number of people who stayed. 
# clearly the lower the job satisfaction level, the higher the ratio. 
def percent(x):
    return (x['Yes']/x['No'])*100
attr_jobSatisfaction.apply(percent, axis=0).plot.bar(figsize=(7, 5), xlabel='Job Satisfaction', ylabel='Percentage_attrition',rot=0)

# 3. Attrition results on EducationField
# a) Percentage difference on EducationFields
df_categorical['EducationField'].value_counts().plot.pie(figsize=(7, 5), autopct='%.2f%%', rot=0)
# b) Attrition comparison on EducationFields
attr_eduField = df_categorical[['Attrition', 'EducationField']].value_counts().unstack()
percentage_eduField_attr = attr_eduField/attr_eduField.apply(sum, axis=0)*100
percentage_eduField_attr.loc['No'].plot.bar(figsize=(9, 6), rot=0)
percentage_eduField_attr.loc['Yes'].plot.bar(figsize=(9, 6), rot=0)
