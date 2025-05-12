import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,1)
axes.plot(
    [2.0,4.0,8.0,10.0],
    [1.0,3.0,2.0,6.0],
    color="red",linestyle="--"
)
plt.show()