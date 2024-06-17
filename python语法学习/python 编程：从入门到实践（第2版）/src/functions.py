# chapter08

print('\n定义函数')
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}")

greet_user('shishao')

# 变量 username 是一个形参
# ‘shishao’ 是一个实参


# ...... 省略不重要的


print('\n传递任意数量的实参')
def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print(topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')



#有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
#在这种情况下，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少。
print('\n使用任意数量的关键字实参')
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    
user_profile = build_profile('albert', 'einstein',
    location='princeton',
    field='physics')
print(user_profile)