# 1. 用方括号（[]）表示列表，并且用逗号分隔其中的元素

# 2. 列表是有序集合，按元素的位置（索引）访问某个元素


# 在列表末尾添加元素
lt = [1, 2, 3]
lt.append(4)
print(lt)


# 在列表中插入元素
lt = [1, 2, 3]
lt.insert(0, 5)
print(lt)


# 删除元素
# 1. 使用 del
lt = [1, 2, 3]
del lt[1]
print(lt)
# 2. 使用 pop
lt = [1, 2, 3]
lt.pop()
print(lt)
get_pop = lt.pop(0) #指定要删除的
print(lt, "get_pop=", get_pop)

# 根据值删除元素
motor_cycles = ['honda', 'yamada', 'suzuki', 'ducati']
motor_cycles.remove('yamada')
print(motor_cycles)



# ------------------------ 组织列表 ------------------------
# 1. 方法sort() -- 对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 函数可以添加参数：reverse=True
print(cars)

# 2. 方法sorted() -- 临时改变排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
new_cars = sorted(cars)
print("cars=", cars, "new_cars=", new_cars)

# 3. 反转列表
cars.reverse()
print(cars)

# 4. 获取列表的长度
print("cars's len = ", len(cars))



# ------------------------ 操作列表 ------------------------
lt = [1, 2, "3", 4, 5, 6]
for item in lt:
    print(item)


# 创建数值列表
print('创建数值列表')
for value in range(1, 6):
    print(value)


# 使用 range() 创建数字列表
numbers = list(range(1, 6))
print(numbers)


numbers = list(range(2, 10, 2)) #指定步长
print(numbers)


# squares.py
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 列表解析 --  列表解析让你只需编写一行代码就能生成 上面的列表
squares = [value**2 for value in range(1, 11)]
print("列表解析：", squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min = min(digits)
print(min)
max = max(digits)
print(max)
sum = sum(digits)
print(sum)



# 使用列表的一部分 -- 切片



# 元组  ---  Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组
# 元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。