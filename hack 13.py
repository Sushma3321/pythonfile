a=[0,1,0,3,12]
i=0
c=[]
while i<len(a):
    if a[i]>0:
        c.append(a[i])
    i=i+1
j=0
while j<len(a):
    if a[j]==0:
        c.append(a[j])
    j=j+1
print(c)
