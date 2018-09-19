# def h():
#     print(1)
#     return 0
# h()
# def h(a):
#     print('1'*a)
#     return 0
# h(3)
# def h(a,b):
#     #print(a*b/2)
#     return a*b/2
# h(1,2)
# def h(a,b,c):
#     # print(a*b*c)
#     return a*b*c
# print(h(1,2,3))
# def h(a,b):
#     if a*b/2>10:
#         print('大')
#     elif a*b/2<=10 and a*b/2>0:
#         print('小')
#     else:
#         print('非法')
# h(1,2)
# h(4,5)
# h(-1,9)

# def judge(a,b):
#     if a*b<0:
#         print("error")
#         return 0
#     if a*b>0 and a*b<=10:
#         print ("little trangle")
#         return 0
#     if a*b>10:
#         print("big trangle")
#         return 0
# print(judge(5,7))

# a=[1,2,3,4,5,6]
# def b(a):
#     a.append(9)
#     return a
# print(b(a))
# print(a)
# a={1:2,3:4,5:6}
# def b(a):
#     a[7]=8
#     return a
# print(b(a))
# print(a)
# def a(a):
#     print(a)
# a(1)
# def h(b,*a):
#     print(*a)  # *代表不定长参数，类似列表
# h(1,2,3,4)
# def a(b):
#     if b==1:
#         return b
#     elif b>1:
#         return b+a(b-1)
#     else:
#         return b+a(b+1)
# print(a(10))
# print(a(-10))
# print(a(1))
# def a(c):
#     if c==2:
#         return c
#     elif c>2:
#         c = a(c - 1) + a(c - 2)
#         return c
#     else:
#         return 0
# print(a(10))
# print(a(-10))
# # def a(b):
#     if b==1:
#         return 1
#     elif b>1:
#         return 2*a(b-1)
#     else:
#         return 0
# print(a(29))
# print(a(30))
# if a(30)/a(29)==2:
#     print(1)
# else:
#     print(2)
# a=lambda x,y:x*x+y+1
# print(a(1,5))  #x,y只能是是整数类或浮点类，不能是字符串类型
# name='1'
# def a():
#     print(name)
# def b():
#     name='2'
#     print(name)
#     a()    #a()这时调用的是全局变量name
# b()
# i=3
# def a():
#     i=1
#     def b():
#         nonlocal i
#         # global i
#         i=2
#         print(i)
#     b()
#     print(i)
# a()
# print(i)