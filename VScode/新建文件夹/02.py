# import os
# os.chdir("C:\\Users\\lenovo\\Desktop")
# print(os.getcwd())

# str = "this is really a string example....isw!!!"
# substr = "is"


# print(str.rfind(substr,10,0))
with open(r'C:\Users\lenovo\Desktop\www.csv','r') as fo:
    # for i in range(4):
    #     fo.readline()
    #     if i == 1:     #想要的行数减一
    #         print(fo.readline())
    i = 0
    for g in fo:
        if i == 2:
            print(g)
        i += 1