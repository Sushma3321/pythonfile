# num=int(input("enter the number"))
i=0
c=0
while i<=10:
    a=i%10
    if a==2 or a==9 or a==3:
        c=c+1
    i=i+1                                          
print(c)
