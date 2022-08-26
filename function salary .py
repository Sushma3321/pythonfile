# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")


# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")



def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
        return sum

print(sumofdigits(123))