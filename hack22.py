string="abcd"

i=0
while i<=len(string):
    if string[i]==string[-i+1]:
        print("polindrome")
        break
    else:
        print("not polindrome")
        break
    i=i+1

