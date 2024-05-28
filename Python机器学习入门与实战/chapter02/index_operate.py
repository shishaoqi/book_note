import numpy as np

#基本的索引



#切片索引



#布尔型索引
names=np.array(["业务员","业务员","经理","主管","业务员","主管"])
salary=np.array([2520.00,3600.00,2745.00,4200.00,3805.00,3947.00])
print(salary[names!="业务员"])
print("----------------------------") 
print(salary[~(names=="业务员")])

#代码中使用了salary[names!="业务员"]语句，用"!="表示names数组中不是“业务员”职位的人员；
#也使用了salary[~(names=="业务员")]语句，用“~”表示同样的意思。