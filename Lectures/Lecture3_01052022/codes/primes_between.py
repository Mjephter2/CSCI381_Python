# prime numbers between 1 and 100
for i in range(101):
    isPrime = True
    j = 2
    while(j < i):
        if(i % j == 0):
            isPrime = False
            break
        j += 1
    if isPrime:
        print(i)

