def add(a, b):
    print('this is add function')
    return a + b

x = 1
y = 2

r = add(x, y)
print(r)

#利用 Python 动态执行的特性
cond = False
if cond:
    def divide(x, y):
        return x / y
else:
    def divide(x, y):
        return x % y
    
print(divide(2, 5))
#依赖类型的行为称为多态