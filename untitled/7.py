# class a:
#     h=2
#     def __init__(self,first,last,email,k='funcat.com'):
#         self.first=first
#         self.last=last
#         self.email=first+last+'@'+k
#     def b(self):
#         print(self.email)
# c=a('d','e','f')  #要先实例化，再调用方法，否则会报错
# c.b()  #方法必须加括号

# 声明一个Employee 类
# class Employee:
#     # 声明一个类的变量
#     pay_raist_amount = 1.2
#     # 创建一个构造器
#     def __init__(self,first,last,pay,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain
#
#     # 创建一个方法
#
#     def fullname(self):
#         return self.first+self.last
#
#     def new_pay0(self):
#         # return self.pay * Employee.pay_raist_amount
#         return self.pay * self.pay_raist_amount   #在class外重新赋值，可被改变
#
#     def new_pay1(self):
#         return self.pay * Employee.pay_raist_amount    #在class外重新赋值，不会被改变
#
#
#
# # 创建一个类的实例
# emp1 = Employee("xiaoming","wang",10000,"baidu.com")
# emp2 = Employee("xiaohong",'zhang',20000)
# Employee.pay_raist_amount = 1.4    #将类内部全局变量修改了，全部实例调用类的变量都会被改变
# print(emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())
# emp1.pay_raist_amount = 1.5
# print("emp1. raise, emp1.newpay0()",emp1.new_pay0())
# print(emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())
# emp2.pay_raist_amount = 1.6
# print(emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())
# 声明一个Employee 类
# class Employee:
#     # 声明一个类的变量
#     pay_raist_amount = 1.2
#
#     __weight = 40
#     # 创建一个构造器
#     def __init__(self,first,last,pay,weight,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain
#         self.__weight = weight
#
#     def __say(self):
#         print("helloworld {}".format(self.__weight))
#
#     def Isay(self):
#         self.__say()
#
#     # 创建一个方法
#     def fullname(self):
#
#         return '{}-{}-{}'.format(self.first,self.last,self.pay)
#
#     def new_pay0(self):
#         # return self.pay * Employee.pay_raist_amount
#         return self.pay * self.pay_raist_amount
#
#
#
# # 创建一个类的实例
# emp1 = Employee("xiaoming","wang",10000,50,"baidu.com")
#
# # emp1.__weight = 60
# # emp1.__say()
# emp1.Isay()
# # emp2 = Employee("xiaohong",'zhang',20000)
# # print(emp1.fullname())

# class a:
#     def __s(self):
#         print(1)
#     def t(self):
#         self.__s()    #调方法要括号
#     __q=1
#     def u(self):
#         print(self.__q)
# w=a()
# w.t()
# w.u()
# class People:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#
# class Student(People):
#
#     def __init__(self,n,a,w,grade):    #默认值全部放最后
#         # People.__init__(self,n,a,w)
#         super().__init__(n,a,w)
#         self.grade = grade
#
#     # 方法重写
#     def speak(self):
#         print("%s说: 我 %d 岁, %d 年级" %(self.name,self.age,self.grade))
# #默认值全部放最后
#
#
# s = Student('xiaoming',20,50,5)
# s.speak()
class a:
    def __init__(self,b,c,d):
        self.b=b
        self.c=c
        self.d=d
    def e(self):
        print(1)
class f(a):
    def __init__(self,b,c,d,g):
        self.g=g
    def e(self):
        print(2)
class k(a):
    def __init__(self,b,c,d,h,i):
        self.h=h
        self.i=i
    def e(self):
        print(3)
    def __l(self):
        print(5)
class v(f,k):    #只能调用头一个被继承类的__init__函数
    def e(self):
        print(4)
    def m(self):
        self.__l()
s=v('a',1,2,3)
s.e()
# s.m()    #私有方法、私有属性只能在父类中调用，不能在子类中调用