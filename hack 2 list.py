# The chef's phone shows a Battery Low notification if the battery level is 15% or less. Given that the battery level of Chef's phone is X%, determine whether it would show a Battery low notification.
level=int(input("enter the level"))
if level<=15:
    print("your battery is low")
else:
    print("no")
