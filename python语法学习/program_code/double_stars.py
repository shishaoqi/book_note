# 1. 接收任意数量的关键字参数

# 当函数需要接收任意数量的 "关键字参数"（即命名参数）时，可以使用 **kwargs 来捕获所有未明确在函数定义中声明的关键字参数。这些参数会被存储在一个字典（dict）中。
def function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function_with_kwargs(name='John', age=24, addr='xiameng')


# 2. 接收任意数量的位置参数（*args）

# 当函数需要接收任意数量的位置参数（即不命名的参数）时，可以使用 *args 来捕获。这些参数会被存储在一个元组（tuple）中。

def function_with_args(*args):
    for arg in args:
        print(arg)


function_with_args(1, 2, 3, 4)


# 同时使用以上两种用法
# 在这个例子中，flexible_function 可以接收任意数量的位置参数和关键字参数。使用 *args 来接收所有位置参数，使用 **kwargs 来接收所有关键字参数。
def flexible_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

flexible_function(1, 2, name='John', age=25)