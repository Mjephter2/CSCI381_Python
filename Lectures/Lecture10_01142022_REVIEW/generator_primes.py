
def prime_generator():
    primes = [2]

    def is_prime(num):
        answer = True
        for j in primes:
            if(num % j == 0):
                answer = False
                break
        return answer

    while True:
        current_prime = primes[len(primes)-1]
        yield current_prime
        current_prime += 1
        while( not is_prime(current_prime)):
            current_prime += 1
        primes.append(current_prime)

primes = prime_generator()

for i in range(10):
    print(next(primes))
