def max_min(list):
    i=0
    max=list[0]
    min=list[0]
    while i<len(list):
        if list[i]>max:
            max=list[i]
        elif list[i]<min:
            min=list[i]
        i=i+1
    print(max)
    print(min)
    print("diferences",max-min)
max_min([1,2,3])

