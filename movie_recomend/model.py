import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#data preprocessing
movies=pd.read_csv('movies.csv')
credits=pd.read_csv('credits.csv')

df1=pd.DataFrame(movies)
#print(df1.iloc[0])

df2=pd.DataFrame(credits)
#print(df2.iloc[0])

df=df1.merge(credits)
#print(df.iloc[0])
print(df)
