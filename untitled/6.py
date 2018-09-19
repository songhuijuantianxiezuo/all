class animal:
    def __init__(self,name):
        self.name=name
        print('I am a annimal')
    def eat(self):
        print(self.name,'is eating')
    def drink(self):
        print(self.name,'is drinking')
class elephent(animal):
    def __init__(self,name):
        self.name=name
        print('I am an elephent')
    def water(self):
        print(self.name,'need water')
class human(animal):
    def __init__(self,name):
        self.name=name
        print('I am a human')
    def move(self):
        print(self.name,'like moving')
    def love(self):
        print(self.name,'love you')
class student(human):
    def __init__(self,name):
        self.name=name
    def study(self):
        print('I like studying')
class teacher(human):
    def __init__(self,name):
        self.name=name
    def teach(self):
        print('I like teaching')
zhanglang=animal('zhanglang')
zhanglang.eat()
zhanglang.drink()
daxiang=elephent('daxiang')
daxiang.water()
daxiang.drink()
daxiang.eat()
wo=human('wo')
wo.eat()
wo.move()
wo.drink()
wo.love()
xuesheng=student('xuesheng')
xuesheng.love()
xuesheng.study()
xuesheng.drink()
laoshi=teacher('laoshi')
laoshi.teach()
laoshi.love()