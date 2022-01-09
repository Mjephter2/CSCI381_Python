num = eval(input("Enter a four digits number "))

if 1000 <= num <= 9999:
    numCopy = int(num)
    lastDigit = numCopy % 10
    numCopy = numCopy // 10

    thirdDigit = numCopy % 10
    numCopy = numCopy // 10

    secondDigit = numCopy % 10
    numCopy = numCopy // 10

    firstDigit = numCopy % 10
    numCopy = numCopy // 10

    if(firstDigit == lastDigit and secondDigit == thirdDigit):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
else:
    print("bad input")