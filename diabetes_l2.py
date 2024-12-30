from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

#loading and organizing the dataset
diabetes=load_diabetes()
df=pd.DataFrame(data=diabetes.data,columns=diabetes.feature_names)
df['target']=diabetes.target

#defining the variables
X=diabetes.data
Y=diabetes.target

#train test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.35, random_state=42)

#scaling the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

#ridge regression
ridge_reg=Ridge()
params={'alpha':[2,5,10,1,30,40,50,60]}
ridge_cv=GridSearchCV(ridge_reg,params,scoring='neg_mean_squared_error',cv=5)#trainin the ridge_reg model with cross validation
ridge_cv.fit(X_train,Y_train)

#print(ridge_cv.best_params_)
#print(ridge_cv.best_score_)#mse in this case is 3868 which is more than the one found in plain regression 3167

#prediction
reg_pred=ridge_cv.predict(X_test)
'''we observed different values when using ridge_reg.predict() and ridg_cv.predict() because ridge_cv is the 
trained version of ridge_reg
'''
#visulazation
import seaborn as sns
sns.displot(reg_pred-Y_test,kind="kde")
plt.show()

#r2 score
from sklearn.metrics import r2_score
r2=r2_score(Y_test,reg_pred)
#we get r2 score of 51.2% which is higher than that in plain linear regression 47.7%.which indicates better performance
print(f"r2 score is {r2}")
