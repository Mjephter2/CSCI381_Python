def primes_between():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    line_count = 0

    for i in range(num1, num2 + 1, 1):
        is_prime = True
        j = 2
        while(j < i):
            if(i % j == 0):
                is_prime = False
                break
            j += 1
        if is_prime:
            if line_count < 4:
                line_count += 1
                print(i, end=" ")
            else:
                line_count = 0
                print(i)
    print()
primes_between()
