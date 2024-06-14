name = "hello world"
print(name.title())
print(name.upper())
print(name.lower())


#在字符串中使用变量 -- 类同：C 或 go  sprintf() 方法
first_name = "shi"
last_name = "shao"
full_name = f"{first_name} {last_name}" # f 是 format 的缩写
print(full_name)
print(f"hello, {full_name.title()}")
# f字符串是Python 3.6引入的
# 如果你使用的是Python 3.5或更早的版本，需要使用format() 方法，而非这种f语法
full_name = "{} {}".format(first_name, last_name)
print("format() output: ", full_name)

# 制表符 与 换行符
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# 删除空白
blank = 'python '
print(blank)
blank.rstrip()
print(blank)
# 可以剔除字符串开头的空白，或者同时剔除字符串两边的空白。为此，可分别使用方法lstrip() 和strip()