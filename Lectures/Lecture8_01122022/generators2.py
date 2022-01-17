import random
n = int(input("Enter first number: "))
m = int(input("Enter second number that is > " + str(n) + ": "))

def random_generator(m):
    while True:
        yield random.randint(1, m)

gnrtor = random_generator(m)

my_list = []
for i in range(n):
    my_list.append(next(gnrtor))

print(my_list)