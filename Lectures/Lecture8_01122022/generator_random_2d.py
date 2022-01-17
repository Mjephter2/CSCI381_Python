import random
n = int(input("Enter first number: "))
m = int(input("Enter second number that is > " + str(n) + ": "))

k = m * n

def random_generator(max):
    seen = []
    while True:
        generated = random.randint(1, max)
        while generated in seen:
            generated = random.randint(1, max)
        yield generated
        seen.append(generated)

gnrtor = random_generator(k)

my_list = []

# initialize list
for i in range(n):
    my_list.append(0 * [0])

for i in range(n):
    for j in range(m):
        my_list[i].append(next(gnrtor))

def print_matrix(m, size1, size2):
    for i in range(size1):
        print("\t[", end='')
        for j in range(size2):
            print(format(m[i][j], "3.0f"), "", end="")
        print("]")
        
print_matrix(my_list, n, m)
