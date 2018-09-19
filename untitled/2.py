# i=1
# j=1
# while i<2000:
#     while j<2000:
#         i,j=j,i+j
#         print(i,j)
# list1=[1,2,7,4]
# i=0
# for a in list1:
#     for b in list1:
#         for c in list1:
#             for d in list1:
#                 if a!=b and b!=c and c!=d and b!=d and a!=c and a!=d:
#                      e=1000*a+100*b+10*c+d
#                      print(e)
#                      i+=1
# print(i)
a=[]
b=0
for i in range(0,10):
    if i%2==1:
        b+=1
        a.append(i)
print(a)
# a=[i for i in range(1,10,2)]   # 列表生成式
# print(a)
