# 基本数据类型之间的 嵌套

# 例一
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# 例二： 使用 range() 生成 30 个外星人
aliens = []

for alien_number in range(30):
    new_alien = {'id': alien_number, 'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print (alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


# 在字典中存储列表



# 在字典中存储字典


