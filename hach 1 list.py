# You are provided an array A of size N  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10
a=[85,25, 65 ,21 ,84]
i=0
c=0
while i<len(a):
    if a[i]%10==0:
        print("yes")
    else:
        b=a[i]%10
        c=c*10+b
        print("the last digit of", b)
    i=i+1
print(c)
if c%10==0:
    print("yes")
else:
    print("no")



