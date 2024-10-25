#声明class
class FirstClass:
    def setdata(self, value):
        self.data = value
    
    def display(self):
        print(self.data)

c1 = FirstClass()
c1.setdata("I'm the King of the world")
c1.display()

c1.data = "New value"
c1.display()

#继承
class SecondClass(FirstClass):
    def display(self):
        super().display() #父方法
        print('Current value = "%s"' % self.data)


c2 = SecondClass()
c2.setdata("I'm the SecondClass")
c2.display()


#类可以截获Python运算符
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirClass: %s]' % self.data
    def mul(self, other):
        self.data *= other


# 最简单的类
class cl: pass


# 类的一般形式
# class <name>(superClass,...)
#     data = value
#     def method(self, ...):
#         self.member = value


