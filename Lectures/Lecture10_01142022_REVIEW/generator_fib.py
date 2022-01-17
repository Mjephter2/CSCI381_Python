
def fibo_generator():
    previous = 1
    current = 1

    while True:
        yield previous
        previous, current = current, current + previous

fib_gen = fibo_generator()

for i in range(20):
    print(next(fib_gen))