def big_word():
    f=open("elabhi.text","r")
    data=f.readline()
    
    a=data.split()
    i=0
    big_word=a[0]
    while i<len(a):
        if a[i]>big_word:
            big_word=a[i]
        i=i+1
    print(big_word)
    print(len(big_word))


big_word() 