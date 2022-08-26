
def anagram(str1,str2):
    a=sorted(str1)
    b=sorted(str2)
    if a==b:
        print("anagram")
    else:
        print("not anagram")
anagram("heart","earth")