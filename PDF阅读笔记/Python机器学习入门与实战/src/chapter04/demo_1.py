import matplotlib.pyplot as plt

fig = plt.figure() #调用上述语句会弹出一个空窗口

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)

ax1.plot(
    [2.0,4.0,8.0,10.0],
    [1.0,3.0,2.0,6.0],
    "k--"
)

plt.show()