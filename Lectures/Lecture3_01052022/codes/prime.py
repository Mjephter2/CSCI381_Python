num = int(input("Enter a positive number greater than 1: "))

if(num < 1):
    print("bad input!")
    exit()
isPrime = True
i = 2
while(i < num):
    if(num % i == 0):
        isPrime = False
        break
    i += 1
if isPrime:
    print(num, "is prime")
else:
    print(num, "is not prime")
