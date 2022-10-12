import scipy.special as sc

a1,b1,a2,b2 = 91,11,3,1
def f1(x1):
    return 1/sc.beta(a1,b1)*x1**(a1-1)*(1-x1)**(b1-1)
def f2(x2):
    return 1/sc.beta(a2,b2)*x2**(a2-1)*(1-x2)**(b2-1)
#原函数
def f(x1,x2):
    f = f1*f2
#导函数
def f_x(x1,x2):
#积分区间
upper_bound=1
lower_bound=0
#生成随机数，用蒙特卡洛方法计算定积分
DefiniteIntegral_By_MonteCarloMethod=0
sum=0
count=1
while count<=10000:
    sum=sum+f_x_(random.uniform(lower_bound,upper_bound))
    count=count+1
DefiniteIntegral_By_MonteCarloMethod=(upper_bound-lower_bound)*(sum/10000)
print("用蒙特卡洛方法计算的定积分：")
print(DefiniteIntegral_By_MonteCarloMethod)