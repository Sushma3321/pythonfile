def my_function(list):
    b=[]
    c=[]
    d=[]
    i=0
    while i<len(list):
        if type(list[i])==int:
            b.append(list[i])
        elif type(list[i])==str:
            c.append(list[i])
        elif type(list[i])==float:
            d.append(list[i])
        i=i+1
    print(b)
    print(c)
    print(d)
my_function(["i", "j", "i", "k" ,"g" ,7 ,6 ,5 ,8.8 ,"j","j","r"])



