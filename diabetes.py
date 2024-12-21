from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

diabetes=load_diabetes()
df=pd.DataFrame(data=diabetes.data,columns=diabetes.feature_names)
#print(df.head())

#classify as independent and dependent features
X=diabetes.data
Y=diabetes.target
print(Y[:5])