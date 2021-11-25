# The question is how salary rise do we need to stay in the company as age increases
# First we divide the dataframe into those who attrited from the company and those who do not.
# Then we plot their age vs their monthly income and compute the regression line for these two groups and compare their difference

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_income_by_x(x_axis:str, df):
    '''
    plot income by col x_axis in attrited and remained groups

    Param:
        y: str
        df: pd.DataFrame
    
    Return:
        None
    '''
    assert isinstance(x_axis, str)
    assert isinstance(df, pd.DataFrame)
    fig, ax = plt.subplots(figsize=(10,7), nrows=1, ncols=2)
    df_attrited = df.loc[df['Attrition'] == 1]
    df_remained = df.loc[df['Attrition'] == 0]

    ax[0].scatter(data=df_attrited, x=x_axis, y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[0].set(title='MonthlyIncome by {}'.format(x_axis), xlabel=x_axis, ylabel='MonthlyIncome')
    ax[1].scatter(data=df_remained, x=x_axis, y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[1].set(title='MonthlyIncome by {}'.format(x_axis), xlabel=x_axis, ylabel='MonthlyIncome')

    #plot regression line
    m, b = np.polyfit(df_attrited[x_axis], df_attrited.MonthlyIncome, 1)
    ax[0].plot(df_attrited[x_axis], m * df_attrited[x_axis] + b, c='sandybrown', label='y={:.2f}x+{:.2f}'.format(m,b))
    ax[0].legend(fontsize=9, loc='upper left')

    m, b = np.polyfit(df_remained[x_axis], df_remained.MonthlyIncome, 1)
    ax[1].plot(df_remained[x_axis], m * df_remained[x_axis] + b, c='sandybrown', label='y={:.2f}x+{:.2f}'.format(m,b))
    ax[1].legend(fontsize=9, loc='upper left')

df = pd.read_csv('./data/preprocessed/HR_Employee_Attrition.csv')
plot_income_by_x('Age', df)
plt.show()
plot_income_by_x('TotalWorkingYears', df)
plt.show()
