# -*- coding: utf-8 -*-
"""Copy of Women's E-Commerce Shopping Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/189GOvMZe2K0z7UcYeOkwZIu8KTqKdDZd
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from google.colab import files
files = files.upload()

import io

df = pd.read_csv(io.BytesIO(files['Womens Clothing E-Commerce Reviews.csv']))

df.head()

df.drop('Unnamed: 0', axis=1, inplace=True)

df.columns

df.isnull().sum()

df['Division Name'].value_counts()

df['Class Name'].value_counts()

df['Department Name'].value_counts()

df.dropna(inplace=True)

df.isnull().any()



"""**DATA VISUALIZATION**"""

plt.figure(figsize = (9,5))
sns.heatmap(df.corr(), annot=True)

plt.figure(figsize = (10,5))
sns.barplot(df['Class Name'].value_counts()[:15].index,df['Class Name'].value_counts()[:15].values)
plt.title('E-Commerce Shopping ')
plt.xlabel('CLass Name')
plt.ylabel('Count')
plt.xticks(rotation= 90)
plt.show()

plt.figure(figsize = (10,5))
sns.barplot(df['Department Name'].value_counts()[:15].index,df['Department Name'].value_counts()[:15].values)
plt.title('E-Commerce shopping')
plt.xlabel('Department Name')
plt.ylabel('E-Commerce Shopping')
plt.xticks(rotation= 90)
plt.show()

plt.figure(figsize = (10,5))
sns.barplot(df['Division Name'].value_counts()[:15].index,df['Division Name'].value_counts()[:15].values)
plt.title('Division Name')
plt.xlabel('E-Commerce shopping')
plt.ylabel('Division Name')
plt.xticks(rotation= 90)
plt.show()

df['Review Text'].head(10)

sns.histplot(data=df, x="Rating")

sns.relplot(x="Age", y="Department Name", data=df)

fig, ax = plt.subplots()
fig.set_size_inches(14, 5)

ax = sns.violinplot(x="Department Name", y="Age", data=df)



"""**Preprocess the Data**"""

def preprocess(ReviewText):
  ReviewText = ReviewText.str.replace("(<br/>)"," ")
  ReviewText = ReviewText.str.replace('(<a).*(>).*(</a>)', '')
  ReviewText = ReviewText.str.replace('(&amp)','')
  ReviewText = ReviewText.str.replace('(&gt)','')
  ReviewText = ReviewText.str.replace('(&lt)', '')
  ReviewText = ReviewText.str.replace('(\xa0)','')
  return ReviewText

from textblob import TextBlob

df['Polarity'] = df['Review Text'].apply(lambda x:TextBlob(x).sentiment.polarity)
df['word_count']= df['Review Text'].apply(lambda x: len(str(x).split()))
df['review_len'] = df['Review Text'].apply(lambda x: len(str(x)))



"""**CHECK MOST POSITIVE, NEG AND NEUTRAL POLARITY REVIEWS**"""

cl = df.loc[df.Polarity == 1, ['Review Text']].sample(5).values
for c  in cl:
  print(c[0])

cl = df.loc[df.Polarity == 0, ['Review Text']].sample(5).values
for c  in cl:
  print(c[0])

cl = df.loc[df.Polarity <= 0.7, ['Review Text']].sample(5).values
for c  in cl:
  print(c[0])

