# coding: utf-8
import os,sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def github_get_data():
    df = pd.read_csv("github_dataset.csv", header=0, thousands=',')
    return df

def github_data_abstract(df):
    scalar_cols = ['repositories', 'language']
    number_cols = ['starts_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors']

    for col in scalar_cols:
        freq = df[col].value_counts()
        print(f"\n---------------{col}列取值频数---------------")
        print(freq)

    print("\n---------------数值属性五数概括---------------")
    five = df.describe().loc['min':'max']
    print(five)

def github_data_views(df):
    #view_by_industry(df)
    sns.histplot(data=df['stars_count'])
    sns.histplot(data=df['forks_count'])
    sns.histplot(data=df['issues_count'])
    sns.histplot(data=df['pull_requests'])
    sns.histplot(data=df['contributors'])
    plt.show()

def github_process_missing_data(df):
    print("处理缺失数据前：")
    df.info()

    #用频数填充空值
    df['language'] = df['language'].fillna(df['language'].mode()[0])

    print("处理缺失数据后：")
    df.info()

github_data = github_get_data()
github_data.info()
github_data_abstract(github_data)
github_data_views(github_data)
github_process_missing_data(github_data)
