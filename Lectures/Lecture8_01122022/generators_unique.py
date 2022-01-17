import random
n = int(input("Enter first number: "))
m = int(input("Enter second number that is > " + str(n) + ": "))

def random_generator(m):
    while True:
        yield random.randint(1, m)

gnrtor = random_generator(m)

my_list = []
for i in range(n):
    generated = next(gnrtor)
    if generated not in my_list:
        my_list.append(next(gnrtor))
    else:
        i -= 1

print(my_list)