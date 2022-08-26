def capital(string):
    i=0
    c=[]
    while i<len(string):
        if string[i]==string[i].upper():
            c.append(i)
        i=i+1
    print(c)
capital("HeLlO")
