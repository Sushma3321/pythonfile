# obj=open("elabhi.text","w")
# obj.write("i love you sushma i will die for you  ")



# my_file2 = open("people2.txt", "w")
# my_file2.write("Abhishek - Gurgaon")
# my_file2.write("Ranveer - Delhi")
# my_file2.close()



# my_file3 = open("people3.txt", "w")
# my_file3.write("Abhishek - Gurgaon\n")
# my_file3.write("Ranveer - Delhi")
# my_file3.close()

# my_file3 = open("test_file.txt", "w")
# my_file3.write("Yahan main kuch likha")
# my_file3.write("\nYaha maine kuch aur bhi likha.")

batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")

for student in batch1_students:
        students_file.write("" + student+"\n")
students_file.close()