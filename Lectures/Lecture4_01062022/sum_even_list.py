def is_even(n):
    return n % 2 == 0

l = []
total_sum = 0
for i in range(1, 11):
    l.append(i)
for i in range(10):
    if is_even(l[i]):
        total_sum += l[i]
print(total_sum)