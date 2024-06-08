# 【程序代码清单 2.28】NumPy模块transpose()方法实现数组转置
import numpy as np

arr=np.array([
    [1,1,1,1,1],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [4,4,4,4,4],
    [5,5,5,5,5]]
)
print(arr)
print("after transpose")

arr_trans = arr.transpose()
print(arr_trans)

#transpose()方法也可以用一个特殊的Ｔ属性来代替，代码如下。
arr_T = arr.T
print("after transpose.T")
print(arr_T)


# y = ax1 + bx2 + cx3 + dx4 式子


network:
    version: 2
    renderer: NetworkManager
    ethernets:
        ens33:
            dhcp4: yes
            addresses:
                - 192.168.2.100/24
            gateway4: 192.168.2.1
            nameservers:
                addresses: [114.114.114.114, 8.8.4.4]