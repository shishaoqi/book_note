
# 如何在Python中创建字典？
print('# Define a blank dictionary with no elements')
blank_dict = {}
print(blank_dict)
print(type(blank_dict))
print('Is dict? ', isinstance(blank_dict, dict))

print('# 列表创建字典')
key_value_pairs = [('a', 1), ('b', 2), ('c', 3)]
d = dict(key_value_pairs)
print(d)

print('# 使用 Python zip() 函数从两个列表创建一个字典')
keys = ['a', 'b', 'c']
valus = [1, 2, 3]
kv_pairs = zip(keys, valus)
print(kv_pairs)
d = dict(kv_pairs)
print(d)

print('# 使用 fromkeys() 函数：该函数创建一个带有键序列和默认值的字典。')
keys = ['name', 'age', 'city']
d = dict.fromkeys(keys, 0)
print(d)


# 如何在 Python 中添加/追加到字典
print('# 向字典添加元素 -- 使用赋值运算符')
d = {'name': 'shishao'}
d['age'] = 30
print(d)

print('# 向字典添加元素 -- 使用 update() 方法')
d = {'name': 'shishao'}
d.update({'age': 23, 'city': 'New York'})
print(d)

print('# 向字典添加元素 -- 使用 ** 运算符')
# ** 运算符允许您将字典“解包”为一组键值对。当您想要将列表或其他可迭代对象中的多个键值对添加到字典时，这非常有用。
keys = ['name', 'age', 'city']
values = ['Varsha Dave', 30, 'New York']

d = {**d, **dict.fromkeys(keys, values)}
print(d)

print('# 向字典添加元素 -- 使用extend()方法')



print('# 向字典添加元素 -- 使用+运算符')



# 如何在Python中对字典进行排序