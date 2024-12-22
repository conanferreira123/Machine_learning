from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import seaborn as sns

#loading the dataset
houses=fetch_california_housing()
df=pd.DataFrame(data=houses.data,columns=houses.feature_names)
df['target']=houses.target
print(df.head())