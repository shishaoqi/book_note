# dog 类
class Dog:
    """模拟小狗"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# 再创建个实例
your_dog = Dog('Lucy', 5)


print('\n')
# -------------- 使用类和实例 --------------------
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # 新增
        """将里程表读数设置为指定的值。"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


print('\n直接修改属性的值')
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print('\n通过方法修改属性的值')
my_new_car.update_odometer(23)
my_new_car.read_odometer()


print("\n继承")
class ElectricCar(Car):
    """电动汽车"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

    def describe_battery(self):
        """给子类定义属性和方法"""
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """重写父类的方法"""
        """电动汽车没有油箱。"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())