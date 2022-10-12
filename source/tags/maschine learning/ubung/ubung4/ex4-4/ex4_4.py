import numpy as np
import pandas as pd

# 这里的skiprows是指跳过前1行, 如果设置skiprows=2, 就会跳过前两行
# Python默认读取的数字的数据类型为双精度浮点数
# comment的是指, 如果行的开头为‘#’就会跳过该行
# usecols是指只使用0,2两列。usecols=(0,1,2,3,4)
# unpack是指会把每一列当成一个向量输出, 而不是合并在一起。unpack=True
train=np.loadtxt('ex4_4_train.csv',
                 float,skiprows=1,delimiter=',',usecols=(0,1),unpack=True)
print (train.shape)
print (train)

val=np.loadtxt('ex4_4_val.csv',
                 float,skiprows=1,delimiter=',',usecols=(0,1),unpack=True)
print (val.shape)
print (val)

test=np.loadtxt('ex4_4_test.csv',
                 float,skiprows=1,delimiter=',',usecols=(0,1),unpack=True)
print (test.shape)
print (test)
