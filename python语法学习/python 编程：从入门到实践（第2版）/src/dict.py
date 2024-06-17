# 在Python中，字典 是一系列键值对。每个键都与一个值相关联，你可使
# 用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字
# 典。事实上，可将任何Python对象用作字典中的值。




# 如果指定的键有可能不存在，应考虑使用方法get() ，而不要使用方括号表示法。



# 遍历字典中的所有键值或（只是 键 or 值）
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")



# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("对比：")
for name in favorite_languages: # 这样是取键
    print(name)

print("-----------------------")

for name in favorite_languages.keys():
    print(name.title())


print('遍历字典中的所有值')
# 遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())



# 可使用一对花括号直接创建: 集合
# 集合中的每个元素都必须是独一无二的
languages = {'python', 'ruby', 'python', 'c'}
print(languages)