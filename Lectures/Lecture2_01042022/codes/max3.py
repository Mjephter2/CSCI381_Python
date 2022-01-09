n1 = eval(input("Please enter the first number: "))
n2 = eval(input("Please enter the second number: "))
n3 = eval(input("Please enter the third number: "))
n4 = eval(input("Please enter the fourth number: "))
n5 = eval(input("Please enter the fifth number: "))

max = int(n1)
if n2 > max:
    max = int(n2)
if n3 > max:
    max = int(n3)
if n4 > max:
    max = int(n4)
if n5 > max:
    max = int(n5)

print(max)