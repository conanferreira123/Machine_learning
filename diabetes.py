from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#load/consider the dataset
diabetes=load_diabetes()
df=pd.DataFrame(data=diabetes.data,columns=diabetes.feature_names)
#print(df.head())

#classify as independent and dependent features
X=diabetes.data
Y=diabetes.target

#train test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

#standardization and normalization
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#linear regression
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,Y_train)

#cross validation
from sklearn.model_selection import cross_val_score
mse=cross_val_score(regression,X_train,Y_train,scoring='neg_mean_squared_error',cv=5)
#above is the difference between the predicted value and actual value
print(np.mean(mse))#mean of difference between the predicted values and actual values for different cv cases

#prediction
reg_pred=regression.predict(X_test)

#visualisation
import seaborn as sns
graph=sns.displot(reg_pred-Y_test,kind='kde')
plt.show()

#r2 score to evaluate the models performance
# Evaluate the model on the test set
from sklearn.metrics import r2_score
r2= r2_score(Y_test,reg_pred)
print(f"R² score on the test set: {r2}")
