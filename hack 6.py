# Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell whether he'/ able to complete all assignments on time or not?
user=int(input("enter time when he start"))
user1=int(input("enter the stop time"))
i=0
while i<user:
    if i<user1:
        if (user1-user)<3:
            print("not complete")
            break
        else:
            print("completed")
            break
        i=i+1


