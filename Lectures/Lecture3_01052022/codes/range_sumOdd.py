num = int(input("Enter a positive integer: "))

total = 0

for i in range(1, num + 1, 2):
    total += i

print("sum of odd integers is: ", total)