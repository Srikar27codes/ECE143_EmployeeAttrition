# ttest.py
# analyse numerical columns, applying two sample t tests with p values

import numpy as np
import pandas as pd
from scipy import stats

def ttest(df):
# Data extraction
    df_preprocess = df
    # First select all numerical cols, and divid them into 2 groups: attrited and remained
    df_attrited = df_preprocess.loc[df_preprocess['Attrition']==1].reset_index(drop=True)
    df_remained = df_preprocess.loc[df_preprocess['Attrition']==0].reset_index(drop=True)

    num_col = df_preprocess.select_dtypes('number').columns.to_list()
    cat_col = df_preprocess.select_dtypes(object).columns.to_list()
    num_col.remove('Attrition')

    df_attrited = df_attrited[num_col]
    df_remained = df_remained[num_col]

    # two sample t tests for each numerical columns
    # to select those with p value less than 0.05
    p_vals={}
    for i in num_col:
        mean_attrited=np.mean(df_attrited[i])
        mean_remain=np.mean(df_remained[i])
        # print('mean {0} in attrited group is {1}, while in remain group is {2}'.format(i,str(mean_attrited),str(mean_remain)))
        ttest,pval = stats.ttest_ind(df_attrited[i],df_remained[i])
        p_vals[i]=round(pval,3)
        # print("p-value for {} is: \n".format(i),pval)

    df_pval=pd.DataFrame(p_vals,index=['p_value']).T
    df_pval_reject=df_pval.loc[df_pval['p_value']<=0.05]

    df_pval_reject.to_csv('data/ttest/ttest_outcome.csv')
