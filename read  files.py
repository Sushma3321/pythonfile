# f=open("elabhi.text","r")
# print(f.read())

# f=open("elabhi.text","r")
# print(f.read(5))

# f=open("elabhi.text","r")
# print(f.readline())
# print(f.readline())


# def read():
#     f=open("elabhi.text",'r')
#     while True:
#         s=f.readline()
#         if s=="":
#             break
#         else:
#             print(s)
# read()



def read():
    f=open("elabhi.text","r")
    count=0
    lines=f.readline()
    for i in lines:
        if i[0]=="i":
            count=count+1
    print(count)
    
read()