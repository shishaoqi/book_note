from pandas import Series

obj = Series([28742,39191,28112,37131,26142])
print(obj)

obj_index = obj.index
obj_values = obj.values
print(obj_index)
print(obj_values)

print('通常所创建的Series会采用一个可以对各个数据点进行标记的索引，代码如下')
obj=Series([287345542,391345591,281345512,371345531,261345542], index=["qq_name1","qq_name2","qq_name3","qq_name4","qq_name5"])
print(obj)
print(obj["qq_name2"])

print('根据字典创建')
dicts = {"qq_name1":287892542,"qq_name2":391892591,"qq_name3":281892512,"qq_name4":371892531,"qq_name5":261892542}
obj=Series(dicts)
print(obj)

print('Series这种数据类型的最重要的一个功能是在进行算术运算时会自动对齐不同索引的数据')
goods_in       = Series({"苹果":30,"梨":25,"香蕉":20,"桃":21,"李子":15})
goods_other_in = Series({"苹果":10,"梨":20,"香蕉":15,"桃":10,"西瓜":50})
goods_kucun = goods_in + goods_other_in
print(goods_kucun)
# 如果两个Series相加，索引在两个Series中存在的话，就实现索引对应值的计算；如果其中一个
# Series中有的索引，另一个Series中没有，相加的结果中就会出现NaN（表示空值）这样的值

print('代码中使用Series定义水果超市的库存，其中“李子”的库存量为空，是使用NumPy模块的nan来表示的')
import numpy as np
goods=Series([30,25,20,21,np.nan],index=["苹果","梨","香蕉","桃","李子"])
goods["李子"]=15
print(goods)