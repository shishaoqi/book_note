# and / or 检查多个条件

age_0 = 22
age_1 = 18
age_0 > 21 and age_1 > 21
age_0 > 21 or  age_1 > 21


# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('mushrooms is in ', requested_toppings)
else:
    print('mushrooms is not in ', requested_toppings)

if 'pepperoni' in requested_toppings:
    print('pepperoni is in ', requested_toppings)
else:
     print('pepperoni is not in ', requested_toppings)