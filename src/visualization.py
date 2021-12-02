import pathlib
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def distribution_to_attition(df:pd.DataFrame, col:str, save_path:str='plot'):
    '''
    Split the group into two groups(attrited or not) and plot their distribution for given col

    Param:
        df: pd.DataFrame
        col: str
        save_path: str
    
    Return:
        None
    '''
    assert isinstance(df, pd.DataFrame) and isinstance(col, str) and isinstance(save_path, str)
    assert col in df.columns

    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

    fig = plt.figure()
    ax = sns.kdeplot(x = df.loc[df.Attrition == 0][col], label = "Still Employed", color = "steelblue")
    ax = sns.kdeplot(x = df.loc[df.Attrition == 1][col], label = "Left Company", color = "red")
    min_val=min(df[col])
    max_val=max(df[col])
    ax.set_title('{} comparison among two groups'.format(col))
    ax.set_xlabel(col)
    ax.set_xlim(min_val,max_val)
    ax.set(yticklabels=[])
    ax.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    fig.savefig(save_path + '/{}_distribution_to_attrition.png'.format(col), dpi=fig.dpi)

def monthlyincome_to_col(df:pd.DataFrame, col:str, save_path:str='plot'):
    '''
    First we divide the dataframe into those who attrited from the company and those who do not.
    Then we plot their age vs their monthly income and compute the regression line for these two groups and compare their difference

    Param:
        df: pd.DataFrame
        col: str
        save_path: str
    
    Return:
        None
    '''
    assert isinstance(df, pd.DataFrame) and isinstance(col, str) and isinstance(save_path, str)
    assert col in df.columns

    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12,7), nrows=1, ncols=2)
    df_attrited = df.loc[df['Attrition'] == 'Yes']
    df_remained = df.loc[df['Attrition'] == 'No']

    ax[0].scatter(data=df_attrited, x=col, y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[0].set(title='MonthlyIncome by {}'.format(col), xlabel=col, ylabel='MonthlyIncome')
    ax[1].scatter(data=df_remained, x=col, y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[1].set(title='MonthlyIncome by {}'.format(col), xlabel=col, ylabel='MonthlyIncome')

    m, b = np.polyfit(df_attrited.col, df_attrited.MonthlyIncome, 1)
    ax[0].plot(df_attrited.col, m * df_attrited.col + b, c='sandybrown', label='Regression Line')
    ax[0].legend(fontsize=10, loc='upper left')

    m, b = np.polyfit(df_remained.col, df_remained.MonthlyIncome, 1)
    ax[1].plot(df_remained.col, m * df_remained.col + b, c='sandybrown', label='Regression Line')
    ax[1].legend(fontsize=10, loc='upper left')

    fig.savefig(save_path + '/monthlyincome_to_{}.png'.format(col), dpi=fig.dpi)

def overtime_and_marital_status_to_attrition(df:pd.DataFrame, save_path:str):
    '''
    Plot the overtime to attrition rate for different marital status(all, single, married, divorced)

    Param:
        df: df.DataFrame
        save_path: str

    Return:
        None
    '''
    assert isinstance(df, pd.DataFrame) and isinstance(save_path, str)

    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

    df = df.filter(['OverTime','Attrition','MaritalStatus'], axis=1)
    for status in ["All", "Single","Married","Divorced"]:
        temp_df = df[df["MaritalStatus"]==status] if status != "All" else df
        overtime_df = temp_df[temp_df['OverTime'] =='Yes']
        normal_df = temp_df[temp_df['OverTime'] == 'No']
        fig, ax = plt.subplots(1,2, figsize = (16,4))

        normal_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[0], title = status+": Works Normal Hours")
        overtime_df['Attrition'].value_counts().plot.pie(figsize=(7, 5), colors = ['steelblue','red'], autopct='%.2f%%', rot=0, ax = ax[1], title = status+": Works Overtime")
        fig.savefig(save_path + '/overtime_to_attrition_for_{}_people.png'.format(status), dpi=fig.dpi)

def gender_analysis(df:pd.DataFrame, save_path, str):
    '''
    
    '''

if __name__ == '__main__':
    df = pd.read_csv('../data/preprocessed/HR_Employee_Attrition.csv')
    distribution_to_attition('Age')
    distribution_to_attition('MonthlyIncome')
    distribution_to_attition('DistanceFromHome')

    
