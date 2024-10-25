# 用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号
"This is a string."
'This is also a string.'


# 方法title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写
name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())


# 在字符串中使用变量
first_name = "shi"
last_name = "shao"
full_name = f"{first_name} {last_name}" #要在字符串中插入变量的值，可在前引号前加上字母 f ，再将要插入的变量放在花括号内
print(full_name)
print(f"Hello, {full_name.title()}")


# 删除空白 --- str.strip()、 str.lstrip()、 str.rstrip()
language = ' python '
print(language)
language = language.strip()
print(language)