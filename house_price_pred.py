import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


df=pd.read_csv('canada_per_capita_income.csv')
#to get the column names in the dataset
print(df.columns)
#to find max value from a column in our dataset
max_income=df['per capita income (US$)'].max()
#to find the year corresponding to the maximum income
year_max=df[df['per capita income (US$)']==max_income]['year'].values[0]
print(year_max)