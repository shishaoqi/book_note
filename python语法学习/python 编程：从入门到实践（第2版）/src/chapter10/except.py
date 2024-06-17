try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")



first_number = 0
second_number = 0

while True:
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)