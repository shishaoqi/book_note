#第27章
class Person:
    #我们传入的数据作为构造函数方法的参数附加到一个实例上，
    #并且将它们赋给self以持久化
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

#self-test code
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    print(bob.__class__)
    print(bob.__class__.__name__)

    print(list(bob.__dict__.keys()))
    for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])













