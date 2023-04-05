# coding: utf-8
import os,sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_data():
    df = pd.read_csv("movies_dataset.csv", header=0, thousands=',')
    return df

def data_abstract(df):
    scalar_cols = ['appropriate_for', 'director', 'industry', 'language', 'posted_date', 'release_date', 'run_time', 'title', 'writer']
    number_cols = ['Unnamed: 0', 'IMDb-rating', 'downloads', 'id', 'views']

    for col in scalar_cols:
        freq = df[col].value_counts()
        print(f"\n---------------{col}列取值频数---------------")
        print(freq)

    print("\n---------------数值属性五数概括---------------")
    five = df.describe().loc['min':'max']
    print(five)

    print("\n---------------数值属性缺失值统计---------------")
    print(df[['Unnamed: 0', 'IMDb-rating', 'downloads', 'id', 'views']].isna().sum())

def view_by_industry(df):
    sns.barplot(x='industry', y='Unnamed: 0', data=df,
                palette="Set1",
                errwidth=1.2,
                errcolor="0.1",
                capsize=0.05,
                alpha=0.6)
    plt.show()

def data_views(df):
    #view_by_industry(df)
    sns.histplot(data=df['industry'])
    sns.histplot(data=df['views'])
    sns.histplot(data=df['appropriate_for'])
    plt.show()

def process_missing_data(df):
    #用频数填充空值
    print("处理缺失数据前：")
    df.info()
    df['appropriate_for'] = df['appropriate_for'].fillna(df['appropriate_for'].mode()[0])
    df['director'] = df['director'].fillna(df['director'].mode()[0])
    df['language'] = df['language'].fillna(df['language'].mode()[0])
    df['run_time'] = df['run_time'].fillna(df['run_time'].mode()[0])
    df['storyline'] = df['storyline'].fillna(df['storyline'].mode()[0])
    df['writer'] = df['writer'].fillna(df['writer'].mode()[0])

    #用均值填充空值
    df['IMDb-rating'] = df['IMDb-rating'].fillna(df['IMDb-rating'].mean())

    # 这些列只有一行缺失数值 ，删除这些列为空值的行
    df = df.dropna(axis=0,subset = ["industry", "posted_date", 'release_date', 'title', 'views', 'downloads'])

    print("处理缺失数据后：")
    df.info()

data = get_data()
data.info()
data_abstract(data)
data_views(data)
process_missing_data(data)
