import random
n = int(input("Enter first number: "))
m = int(input("Enter second number that is > " + str(n) + ": "))

def random_generator(m):
    while True:
        yield random.randint(1, m)

gnrtor = random_generator(m)

my_list = set()
while len(my_list) < n:
    generated = next(gnrtor)
    if generated not in my_list:
        my_list.add(next(gnrtor))

print(my_list)