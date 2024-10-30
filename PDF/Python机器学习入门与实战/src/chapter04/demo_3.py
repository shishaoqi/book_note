import matplotlib.pyplot as plt

# 代码中plot.subplots(1,1)表示只建立一个Figure和一个subplot
# 对象，axes中存的就是一个axes对象，这里直接采用plot()方法即
# 可，plot()前两个参数指的是横坐标列表和纵坐标列表，“r--”就是
# 颜色和线型构成的字符串，“r”代表红色，“--”代表虚线，“r--”就代表红色虚线
fig,axes=plt.subplots(1,1)
axes.plot([2.0,4.0,8.0,10.0],[1.0,3.0,2.0,6.0],"r--")
plt.show()