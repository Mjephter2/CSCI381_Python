
# not an infinite loop
# when next is called, while loop is ran once
def square(n):
    while True:
        k = n**2
        yield k 
        n += 1
        
x = square(1)

for i in range(10):
    print(next(x))