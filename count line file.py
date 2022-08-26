files=open("elabhi.text","r")
count=0
charecter=0
numb_words=0
for i in files:
    count=count+1
    charecter=charecter+len(i)
    words=i.split()
# split will give words in list
    numb_words=numb_words+len(words)

print(count)
print(charecter)
print(numb_words)











# files=open("elabhi.text","r")
# lines=0
# letters=0
# num_words=0
# for i in files:
#     lines=lines+1
#     letters=letters+len(i)
#     words=i.split()
#     num_words=num_words+len(words)
    
# print(letters)
# print(num_words)
# print(lines)

# files=open("test_file.txt","r")
# data=files.read()
# vowels=["a","e","i","o","u"]
# upper=0
# lower=0
# vowel=0
# consonant=0
# for i in data:
#     if i.isupper():
#         upper=upper+1
#     if i.islower():
#         lower=lower+1
#     if i  in vowels:
#         vowel=vowel+1
#     if i not in vowels:
#         consonant=consonant+1
# print(upper)
# print(lower)
# print(vowel)
# print(consonant)




f=("elabhi.text","r+")