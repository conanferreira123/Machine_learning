import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


df=pd.read_csv('canada_per_capita_income.csv')
print(df.columns)
max_income=df['per capita income (US$)'].max()
year_max=df[df['per capita income (US$)']==max_income]['year'].values[0]
print(year_max)