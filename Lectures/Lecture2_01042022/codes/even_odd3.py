num = eval(input("Enter an integer: "))
isEven = False
if num % 2 == 0:
    print(num, "is even.")
    isEven = True
if isEven:
    print(num, "is odd.")