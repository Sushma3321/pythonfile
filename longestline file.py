f=open("elabhi.text","r")
longest=""
for i in f:
    if len(i)>len(longest):
        longest=i
print(longest)

