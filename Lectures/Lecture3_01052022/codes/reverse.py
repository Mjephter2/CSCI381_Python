num = eval(input("Enter a three digits number not ending in 0: "))

if 100 <= num <= 999:
    numCopy = int(num)
    print(num, "->", end=" ")
    while numCopy > 0:
        print(numCopy % 10, end="")
        numCopy = numCopy // 10
    print()
else:
    print("Bad Input!")