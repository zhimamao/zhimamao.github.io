# 从 sklearn.datasets 导入波士顿房价数据读取器。
from sklearn.datasets import load_boston
# 从读取房价数据存储在变量 boston 中。
boston = load_boston()
# 输出数据描述。
print(boston.DESCR)


# 从sklearn.cross_validation 导入数据分割器。
from sklearn.model_selection import train_test_split
# 导入 numpy 并重命名为 np。
import numpy as np
X = boston.data
y = boston.target
# 随机采样 25% 的数据构建测试样本，其余作为训练样本。
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=150)
# 分析回归目标值的差异。
print("The max target value is", np.max(boston.target))
print("The min target value is", np.min(boston.target))
print("The average target value is", np.mean(boston.target))

# 从 sklearn.preprocessing 导入数据标准化模块。
from sklearn.preprocessing import StandardScaler
# 分别初始化对特征和目标值的标准化器。
ss_X = StandardScaler()
ss_y = StandardScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理。
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))

# 从 sklearn.linear_model 导入 LinearRegression。
from sklearn.linear_model import LinearRegression
# 使用默认配置初始化线性回归器 LinearRegression。
lr = LinearRegression()
# 使用训练数据进行参数估计。
lr.fit(X_train, y_train[:,0])
# 对测试数据进行回归预测。
lr_y_predict = lr.predict(X_test)

##c.岭回归Ridge
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.01, normalize=True)
model.fit(X_train, y_train)
train_score = model.score(X_train, y_train)  # 模型对训练样本得准确性
test_score = model.score(X_test, y_test)  # 模型对测试集的准确性
print(train_score)
print(test_score)

##b.MLE estimate
# 使用 LinearRegression 模型自带的评估模块，并输出评估结果。
print('The value of default measurement of LinearRegression is', lr.score(X_test, y_test))
# 从 sklearn.metrics 依次导入 r2_score、mean_squared_error 以及 mean_absoluate_error 用于回归性能的评估。
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# 使用 r2_score 模块，并输出评估结果。
print('The value of R-squared of LinearRegression is', r2_score(y_test, lr_y_predict))
# 使用 mean_squared_error 模块，并输出评估结果。
print('The mean squared error of LinearRegression is',
mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))
# 使用 mean_absolute_error 模块，并输出评估结果。
print('The mean absoluate error of LinearRegression is', 
mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))
