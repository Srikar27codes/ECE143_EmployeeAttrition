import pathlib
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def distribution_to_attition(df:pd.DataFrame, col:str, save_path:str='plot'):
    '''
    Split the group into two groups(attrit  ed or not) and plot their distribution for given col

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
    fig.savefig(save_path + '/'+col+'_distribution_to_attrition.png', dpi=fig.dpi)

def monthlyincome_to_totalworkingyears(df:pd.DataFrame, save_path:str='plot'):
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
    assert isinstance(df, pd.DataFrame) and isinstance(save_path, str)

    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12,7), nrows=1, ncols=2)
    df_attrited = df.loc[df['Attrition'] == 1]
    df_remained = df.loc[df['Attrition'] == 0]

    ax[0].scatter(data=df_attrited, x='TotalWorkingYears', y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[0].set(title='MonthlyIncome by TotalWorkingYears', xlabel='TotalWorkingYears', ylabel='MonthlyIncome')
    ax[1].scatter(data=df_remained, x='TotalWorkingYears', y='MonthlyIncome', c='MonthlyIncome', cmap='winter')
    ax[1].set(title='MonthlyIncome by TotalWorkingYears', xlabel='TotalWorkingYears', ylabel='MonthlyIncome')

    m, b = np.polyfit(df_attrited.TotalWorkingYears, df_attrited.MonthlyIncome, 1)
    ax[0].plot(df_attrited.TotalWorkingYears, m * df_attrited.TotalWorkingYears + b, c='sandybrown', label='Regression Line')
    ax[0].legend(fontsize=10, loc='upper left')

    m, b = np.polyfit(df_remained.TotalWorkingYears, df_remained.MonthlyIncome, 1)
    ax[1].plot(df_remained.TotalWorkingYears, m * df_remained.TotalWorkingYears + b, c='sandybrown', label='Regression Line')
    ax[1].legend(fontsize=10, loc='upper left')

    fig.savefig(save_path + '/monthlyincome_to_totalworkingyears.png', dpi=fig.dpi)

def overtime_and_marital_status_to_attrition(df:pd.DataFrame, save_path:str='plot'):
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
    explode = (0,0.1)
    fhbcolors = [sns.color_palette('pastel')[0], sns.color_palette('pastel')[3]]

    for status in ["All","Single","Married","Divorced"]:
        temp_df = df[df["MaritalStatus"]==status] if status != "All" else df
        overtime_df = temp_df[temp_df['OverTime'] ==1]
        normal_df = temp_df[temp_df['OverTime'] == 0]
        fig, ax = plt.subplots(1,2, figsize = (16,4))
        normal_df['Attrition'].value_counts().plot.pie(figsize=(7, 5),
                                                       colors = fhbcolors,
                                                       autopct='%.2f%%',
                                                       rot=0, ax = ax[0],
                                                       title = status+": Works Normal Hours",
                                                       explode=explode)
        overtime_df['Attrition'].value_counts().plot.pie(figsize=(7, 5),
                                                         colors = fhbcolors,
                                                         autopct='%.2f%%',
                                                         rot=0, ax = ax[1],
                                                         title = status+": Works Overtime",
                                                         explode=explode)
        fig.savefig(save_path + '/{}_people_overtime_to_attrition.png'.format(status), dpi=fig.dpi)



def gender_analysis(df:pd.DataFrame, save_path:str='plot'):
    '''
    For different gender, we split them into lower age bracket(<35) and higher(>=35) one. Then compare the difference between male and female

    Param:
        df: pd.DataFrame
        save_path: str

    Return:
        None
    '''
    assert isinstance(df, pd.DataFrame) and isinstance(save_path, str)

    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

    df = df[['Age', 'Gender', 'Attrition']]
    explode = (0,0.1)
    fhbcolors = [sns.color_palette('pastel')[0], sns.color_palette('pastel')[3]]
    mhbcolors = [sns.color_palette('pastel')[0], sns.color_palette('pastel')[3]]

    for gender in ['Male', 'Female']:
        higherAgeBracket = df[(df['Age'] >= 35) & (df['Gender'] == gender)]
        lowerAgeBracket  = df[(df['Age'] < 35)  & (df['Gender'] == gender)]

        fig, ax = plt.subplots(1,2, figsize = (16,5))
        higherAgeBracket['Attrition'].value_counts().plot.pie(figsize=(9, 5),
                                                                colors = fhbcolors,
                                                                autopct='%.2f%%',
                                                                rot=0, ax = ax[1],
                                                                title = "Female: Attrition vs Higher Age Bracket",
                                                                explode=explode)
        lowerAgeBracket['Attrition'].value_counts().plot.pie(figsize=(9, 5),
                                                               colors = mhbcolors,
                                                               autopct='%.2f%%',
                                                               rot=0, ax = ax[0],
                                                               title = "Female: Attrition vs Lower Age Bracket",
                                                               explode =explode)
        fig.savefig(save_path+'/{}_age_bracket_to_attrition.png', dpi=fig.dpi)

if __name__ == '__main__':
    df = pd.read_csv('./data/preprocessed/HR_Employee_Attrition.csv')
    distribution_to_attition(df, 'Age')
    distribution_to_attition('MonthlyIncome')
    distribution_to_attition('DistanceFromHome')
    monthlyincome_to_totalworkingyears(df)
    overtime_and_marital_status_to_attrition(df)
    gender_analysis(df)
