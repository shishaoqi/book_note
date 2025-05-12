import matplotlib.pyplot as plt

#根据特定布局创建Figure 和subplot是一件非常常见的
#任务，于是便出现了一个更为方便的方法，直接使用
#plt.subplots()。它可以创建一个新的Figure，并返回一个含有已创建的subplot对象的NumPy数组

# 代码中plt.subplots(2,2)定义了横向2个subplot，竖向2个
# subplot，同时返回两个参数，一个是创建的Figure，另一个是
# subplot对象的axes数组。接下来对axes数据进行引用，调用plot()方
# 法，传入横坐标的列表和纵坐标的列表，参数k--表明线型是虚线，
# color="b"表示颜色为蓝色
fig, axes = plt.subplots(2,2)
axes[0,1].plot(
    [2.0,4.0,8.0,10.0],
    [1.0,3.0,2.0,6.0],
    "k--",
    color="b"
)
plt.show()