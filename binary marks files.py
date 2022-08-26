import pickle
f=open("student.bin","wb")
dic={}
for i in range(5):
    rollno=int(input("enter roll number"))
    name=input("enter name")
    marks=int(input("enter the number"))
    dic[rollno,marks]=name 
pickle .dump(dic,f)
f.close()
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

    