n1 = eval(input("Please enter the first number: "))
n2 = eval(input("Please enter the second number: "))
n3 = eval(input("Please enter the third number: "))

max = int(n1)
if n2 > max:
    max = int(n2)
if n3 > max:
    max = int(n3)

print(max)