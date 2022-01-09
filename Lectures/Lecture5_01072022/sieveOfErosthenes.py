# Generate all primes between 2 and 100 using the Sieve of Erosthenes algorithm
x = [] # initial list to contain all values from 2 to 100
for i in range(2, 101):
    x.append(i)

print("x ->", x)
index = 0
while index < len(x):
    current_p = x[index]
    for j in x[index + 1:len(x)]:
        if j % current_p == 0:
            x.remove(j)
    index += 1
print("primes ->", x)