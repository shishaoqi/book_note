import numpy as np


# 实现大小相等数组的算术运算 -- 被叫作数组广播的妙用
arr = np.array([[10,20,30],[7,8,9]])
multi_arr=arr*arr
sub_arr = arr - arr
print("大小相等的数组实现乘法")
print(multi_arr)
print("大小相等的数组实现减法")
print(sub_arr)


divide_arr = 100/arr
multi_arr = arr * 0.5
print("数组与标量值的除法运算")
print(divide_arr)
print("数组与标量值的乘法运算")
print(multi_arr)

print("\n数组广播的原则")
#2.3.1　数组广播的原则

#距平是一个大气科学术语，一般是指统计学中通常所称的“离差”，
#也就是一组数据中的某一个数与平均数之间的差。
weathers = np.array([
    [20,21,22,18,19,21,22],
    [18,21,23,19,18,21,13],
    [18,19,22,21,21,17,16],
    [15,18,20,19,21,18,18] # 把倒数第二个从17改为18，让数据好观察
])
print('\nmean(0): ', weathers.mean(0))
meaned=weathers-weathers.mean(0) # y轴（列方向） -- mean(0)是在0轴上进行广播
print('\n', meaned)
print('\n', meaned.mean(0))


weathers = np.array([
    [20,21,22,18,19,21,22],
    [18,21,23,19,18,21,13],
    [18,19,22,21,21,17,16],
    [15,18, 20,19,21,17,18]
])
print('\nx轴（行方向）  #reshap((4,1))是把行平均值的开关变成（4，1）:')
print(weathers.mean(1).reshape((4,1))) # x轴（行方向）  #reshap((4,1))是把行平均值的开关变成（4，1）
meaned=weathers-weathers.mean(1).reshape((4,1)) 
print(meaned)
print(meaned.mean(1))
print('\n')

# 创建特殊数组元素值
arr = np.ones((4,6))
arr=arr*5
print(arr)
# 等同法：通过索引位置设置数组元素值
arr = np.ones((4,6))
arr[:]=6
print(arr)