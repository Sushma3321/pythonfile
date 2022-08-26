banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("add fil.text","w") 
# f.write(banks_list[0]+"\n")
# f.write(banks_list[1]+"\n")
# f.write(banks_list[2]+"\n")
for names in banks_list:
        f.write(names+"\n")
f.close
    
