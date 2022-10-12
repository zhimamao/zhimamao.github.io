import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns


# 从 sklearn.datasets 导入波士顿房价数据读取器。
from sklearn.datasets import load_boston
# 从读取房价数据存储在变量 boston 中。
boston = load_boston()
print(boston.keys())
boston['MEDV'] = boston.target
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston['MEDV'], bins=30)
plt.show()
# 从sklearn.cross_validation 导入数据分割器。
from sklearn.model_selection import train_test_split
# 导入 numpy 并重命名为 np。
import numpy as np
X = boston.data
y = boston.target

# 随机采样 25% 的数据构建测试样本，其余作为训练样本。
# train 100 = 0.2,val 50 = 0.1, test 350 = 0.7
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=1)
# 0.125*0.8 = 0.1
X_train, X_val, y_train, y_val  = train_test_split(X_train, y_train, test_size = 1/3, random_state=1)
print(X_train.shape, X_test.shape,X_val.shape,  y_val.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit( X_train, y_train )



#To fit the linear regression model, we selected those characteristics that were highly correlated with our target variable MEDV. A look at the correlation matrix shows that RM has a strong positive correlation with MEDV (0.7), while LSTAT has a strong negative correlation with MEDV (-0.74).
#When selecting characteristics for a linear regression model, it is important to look for multicollinearity. The correlation of the characteristics RAD, TAX is 0.91. These pairs of characteristics have a strong correlation with each other. We should not select both features to train the model. See this explanation. The same applies to DIS and AGE, which have a correlation of -0.75.
#Based on these observations, we used RM and LSTAT as our features
plt.figure(figsize=(20, 5))



#3
from sklearn.linear_model import Ridge
rr = Ridge(alpha=1) #a higher value of alpha restricts the coefficients further
rr.fit(X_train,y_train)
Y_pred_train = rr.predict(X_train) #predictions on training data
Y_pred = rr.predict(X_test) #predictions on testing data
# We plot predicted Y (y-axis) against actual Y (x-axis). Perfect predictions will lie on the diagonal. We see the diagonal trend, suggesting a 'good' fit

plt.scatter(y_test,Y_pred)
plt.xlabel("Actual Price: $Y_i$")
plt.ylabel("Predicted Price: $\hat{Y}_i$")
plt.title("Predicted Price vs Actual Price: $Y_i$ vs $\hat{Y}_i$")
plt.show()

#Training and testing the model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
# model evaluation for training set
y_train_predict = lin_model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for val set
y_val_predict = lin_model.predict(X_val)
rmse = (np.sqrt(mean_squared_error(y_val, y_val_predict)))
r2 = r2_score(y_val, y_val_predict)

print("The model performance for val set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = lin_model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))