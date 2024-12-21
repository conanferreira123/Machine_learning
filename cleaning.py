import pandas as pd

df=pd.read_csv('sample_data.csv')
print(df.columns)

print(df)
#cleaning  wrong data rows by removing them
for x in df.index:
    if df.loc[x,'Age']<0 or pd.isna(df.loc[x,'Age']):
        df.drop(x,inplace=True)

print(df.to_string())

#removing empty cells
