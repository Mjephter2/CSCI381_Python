num = int(input("Enter a 3 digits number: "))
numCopy = int(num)

firstDigit = num//100
num -= num//100*100

secondDigit = num//10
num -= num//10*10

thirdDigit = num

print(numCopy, " -> ", thirdDigit, secondDigit, firstDigit, sep="")