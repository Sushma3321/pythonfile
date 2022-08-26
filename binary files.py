import pickle
f=open("student.bin","wb")
dic={}
for i in range(5):
    rollno=int(input("enter roll number"))
    name=input("enter name")
    dic[rollno]=name
pickle .dump(dic,f)
f.close()
#read binary file
f=open("student.bin","rb")
d=pickle.load(f)
r=int(input("enter roll number to search the student name"))
for key in d:
    if key==r:
        print("enter the roll number",key, "in",d[key])
    if r not in d :
        print("not exist")
        break
f.close()