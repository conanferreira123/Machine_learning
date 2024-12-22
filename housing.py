from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
houses=fetch_california_housing()
df=pd.DataFrame(data=houses.data,columns=houses.feature_names)
df['target']=houses.target
print(df.head())

#defining independent and dependent variables
X=houses.data
Y=houses.target

#train test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.33, random_state=42)

#scaling the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#apply the ml model(linear regression)
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,Y_train)

#cross validation
from sklearn.model_selection import cross_val_score
mse=cross_val_score(regression,X_train,Y_train,scoring='neg_mean_squared_error',cv=6)

#prediction
reg_pred=regression.predict(X_test)

#visulization
import seaborn as sns
sns.displot(reg_pred-Y_test)
plt.show()

#model performance evaluation using r2 score
from sklearn.metrics import r2_score
r2=r2_score(Y_test,reg_pred)
#r2 score of 0.59577 i.e. moderate performance
print(f"r2 score is {r2}")