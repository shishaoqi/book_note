import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr = np.array([1, 2, 3, 4, 5], complex) #复数类型
arr = np.array([1, 2, 3, 4, 5], dtype = None, copy = True, order = None, subok = False)
# 带ndim会报错，---> python3 中无 ndim 参数选项
print(arr)

#从结构上看，每个数组都有一个shape(一个表示各维度大小的元组）
# 和一个dtype(一个用于说明数组数据类型的对象）。
lists1=[[101,202,303], [404,505,606]] 
arr1=np.array(lists1)
print("数组arr1的数据类型是：")
print(arr1.dtype)
print("数组arr1的数组形状是：")
print(arr1.shape)

# zeros((x, y))方法可以新建全0的数组
arr2 = np.zeros((3, 6))
print(arr2)
# ones()方法可以新建全1的数组
# eye(x)方法新建x行x列的数组，并且对角线上的数值为1（其余为0）
# identity(x)方法等同eye(x)
# empty()可以创建没有任何具体值的数组。要用这个方法创建多维数组，只需传入一个表示形状的元组
# empty()返回的是没有意义的数值的数组，其元素不进行初始化，也可以理解成未初始化的“垃圾值”。


# 数据类型转换
arr3=np.array([12.5,136.7,24.6,35.5,109.8]) 
int_arr=arr3.astype(int) 
print(int_arr.dtype) 
str_arr=arr3.astype(str) 
print(str_arr.dtype)


# 随机数生成数组
samples = np.random.normal(size=(4,4))
print(samples)
#而Python内置的random模块则一次只能生成一个样本值。从下面代码的运行结果中可以看出，
#如果需要产生大量的样本值，使用NumPy的random模块执行时间快了不止一个数量级。
from random import normalvariate
import time 
n = 1000000
start = time.time()
samples = [normalvariate(0,1) for _ in range(n)]
times = np.random.normal(size=n)
end=time.time()
print(end-start)

