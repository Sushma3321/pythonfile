# Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.( Consider minimum age of voting to be 18. )
user=int(input("enter the number"))
def eligibleforvote():
    if user>=18:
        print("you are eligible")
    else:
        print("you are not eligible")
eligibleforvote()
