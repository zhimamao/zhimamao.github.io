import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import beta, expon, gamma, laplace, norm

#Aufgabe 6.
#(a) Normal distribution: N (5, 1.5). Plot interval: [0, 10]
plt.figure(1) #第一题
plt.subplot(1, 2, 1) #图一包含1行3列子图，当前画在第一行第一列图上
u = 5  # 均值μ
sig = math.sqrt(1.5)  # 标准差δ
base = 1000
x = np.linspace(0, 10, 50)   # 定义域
y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2*math.pi)*sig) # 定义曲线函数
plt.plot(x, y, "g", linewidth=2)    # 加载曲线
plt.grid(True)  # 网格线
plt.show()  # 显示
plt.figure(1)
plt.subplot(1, 2, 2) #图一包含1行3列子图，当前画在第一行第2列图上 
np.random.seed(0)
s =np.random.normal(u,sig,base)
bins = np.arange(0,11,2)
plt.hist(s,bins)
plt.show()
#(b)Laplace distribution: Laplace(5, 1.5). Plot interval: [−5, 15]
plt.figure(2)
plt.subplot(1, 2, 1)
x = np.linspace(-5, 15, 50)
y = np.exp(-abs(x-u)/sig)/(2.*sig)
plt.plot(x, y, "g", linewidth=2)#
plt.grid(True)  # 网格线
plt.show()  # 显示
plt.subplot(1, 2, 2)
s = np.random.laplace(u, sig, base)
bins = np.arange(-5,16,2)
plt.hist(s,bins)
plt.show()

#(c)Exponential distribution: Exp(0, 1/1.5). Plot interval: [−1, 8]
#期望0;方差1/1.5 =a^-2 ----> a =1.5^2 (a is lambda)
plt.figure(3)
plt.subplot(1, 2, 1)
x = np.linspace(-1,8,1000)
a = 1.5*1.5
#分段函数
interval0 = [0 if(i <  0 )else 0 for i in x]
interval1 = [1 if(i >= 0 )else 0 for i in x]
y = 1 *interval0 +a*np.exp(-a*x)*interval1
plt.plot(x,y)
plt.grid(True)  # 网格线
plt.show()  # 显示
plt.subplot(1, 2, 1)
bins = np.arange(-1,8,2)
plt.hist(y,bins)
plt.show()
#(d) Gamma distribution: Gamma(5, 0, 1). Plot interval: [0, 15]
plt.figure(4)
plt.subplot(1, 2, 1)
x = np.linspace(0,15,1000)
y = scipy.stats.gamma.pdf(x,5,0.1)
