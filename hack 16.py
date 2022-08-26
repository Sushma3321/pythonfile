list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
i=0
c=[]
while i<len(list1):
    if list1[i] in list2:
        c.append(list1[i])
    i=i+1
print(c)