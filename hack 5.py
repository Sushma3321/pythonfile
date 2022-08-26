# Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with him. The cost of 1 chocolate is Y rupees.
chacolate_have=int(input("enter the how many chacolate he have"))
chacolate_want=int(input("enter how many chacolate he wants"))
chacolate_cost=2
i=0
rs=0
while i<chacolate_have:
    if chacolate_want>i:
        rs=(chacolate_want-chacolate_have)*chacolate_cost
    i=i+1
print(rs)