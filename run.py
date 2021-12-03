import pathlib
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import sys

import src.preprocess as preprocess
import src.visualization as visualization
import src.ttest_analysis as ttest_analysis

if __name__ == '__main__':
    # execute the preprocess pipeline
    # processed df has been saved in preprocessed folder
    preprocess.preprocess_df()
    df=pd.read_csv('data/preprocessed/HR_Employee_Attrition.csv')
    # Create analysis and plots for some numeraical cols
    visualization.distribution_to_attition(df,'Age')
    visualization.distribution_to_attition(df,'MonthlyIncome')
    visualization.distribution_to_attition(df,'DistanceFromHome')
    ttest_analysis.ttest(df)
    # Create analysis and plots for categorical cols
    visualization.monthlyincome_to_totalworkingyears(df)
    visualization.overtime_and_marital_status_to_attrition(df)
    visualization.gender_analysis(df)
    sys.exit()
