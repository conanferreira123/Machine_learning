import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


df=pd.read_csv('canada_per_capita_income.csv')
print(df.columns)
max=df['year']['per capita income (US$)'==[df['per capita income (US$)'].max()]]
print(max)