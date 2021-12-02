import pathlib
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

import preprocess
import visualization

if __name__ == '__main__':
    # execute the preprocess pipeline
    # processed df has been saved in preprocessed folder
    preprocess_df()
    df=pd.read_csv('data/preprocessed/HR_Employee_Attrition.csv')

    # Create analysis and plots for some numeraical cols
    distribution_to_attition(df,'Age')
    distribution_to_attition(df,'MonthlyIncome')
    distribution_to_attition(df,'DistanceFromHome')
