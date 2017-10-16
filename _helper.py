import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import collections
import plotly 
import plotly.plotly as py
import plotly.graph_objs as go


def checking_missing(df,Filter):
    """
    check and filter the missing value for each varible in DataFrame
    : type df: pandas.core.frame.DataFrame
    : type Filter: int or boolean
    : rtype: dictionary
    """
    missing_count = {}
    for column in df:
        missing_num = sum(df[column].isnull())
        if missing_num == 0:
            pass           
        elif not Filter:
            missing_count[column] = missing_num
            print('The number of missing value for',column,'is:',missing_num,',','{0:.2f}'.format(missing_num/df.shape[0]*100),'%')
        elif missing_num/df.shape[0]*100 > Filter: 
            missing_count[column] = missing_num
            print('The number of missing value for',column,'is:',missing_num,',','{0:.2f}'.format(missing_num/df.shape[0]*100),'%')
    if not missing_count:
        print('There is no missing value...')
    return missing_count


def correlation_analysis(df, target, source):
    """
    generate correlation heatmap
    : type df: DataFram
    : type target: list # column name
    : type source: list # column name
    """
    matrix_hold = []
    for i in source:
        hold = []
        for j in target:
            hold.append(df[i].corr(df[j]))
        matrix_hold.append(hold)
    correlation_matrix = np.asarray(matrix_hold)
    sns.heatmap(correlation_matrix, xticklabels=target, yticklabels=source)
    plt.title('feature correlations')
    return correlation_matrix


def series_to_freq(series):
    """
    caculate frequence for categorical variables
    : type series: pandas.series
    """
    counter=collections.Counter(series)
    freq_table = pd.DataFrame(list(counter.items()),columns=['category', 'frequence'])
    return freq_table




