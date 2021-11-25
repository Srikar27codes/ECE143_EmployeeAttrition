# deep_analysis.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('data/preprossed/HR_Employee_Attrition.csv')
df = df1.filter(['OverTime','Attrition'], axis=1)
overtime_df = df[df['OverTime'] =='Yes']
normal_df = df[df['OverTime'] == 'No']
fig, ax = plt.subplots(1,2, figsize = (16,4))
normal_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[0], title = "Works Normal Hours")
overtime_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[1], title = "Works Overtime")

df = df1.filter(['OverTime','Attrition','MaritalStatus'], axis=1)
for status in ["Single","Married","Divorced"]:
    temp_df = df[df["MaritalStatus"]==status]
    overtime_df = temp_df[temp_df['OverTime'] =='Yes']
    normal_df = temp_df[temp_df['OverTime'] == 'No']
    fig, ax = plt.subplots(1,2, figsize = (16,4))
    normal_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[0], title = status+": Works Normal Hours")
    overtime_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[1], title = status+": Works Overtime")
    
# Plot job level percentage to those who attrited in male and female group
maleAttrited = df1[(df1['Attrition'] == 'Yes') & (df1['Gender'] == 'Male')]
femaleAttrited = df1[(df1['Attrition'] == 'Yes') & (df1['Gender'] == 'Female')]

def jobLevelNormalize(level):
  '''
  group job level
  '''
  assert isinstance(level, int) and 1 <= level <= 5
  if level <= 2:
    return 'Low'
  elif level >=4:
    return 'High'
  else:
    return "Medium"

maleAttrited['JobLevel'] = maleAttrited['JobLevel'].apply(jobLevelNormalize)
femaleAttrited['JobLevel'] = femaleAttrited['JobLevel'].apply(jobLevelNormalize)

fig, ax = plt.subplots(1,2, figsize = (16,5))
maleAttrited['JobLevel'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue', 'red', 'sandybrown'], autopct='%.2f%%', rot=0, ax = ax[0], title = "Attrited Male")
femaleAttrited['JobLevel'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue', 'red', 'sandybrown'], autopct='%.2f%%', rot=0, ax = ax[1], title = "Attrited Female")
