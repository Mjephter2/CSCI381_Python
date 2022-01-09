num = int(input("How many columns? "))

for i in range(num):
    for j in range(i + 1):
        if i == j:
            print("*")
        else:
            print(" ", end=" ")

for i in range(num - 1, 0, -1):
    for j in range(1, i + 1):
        if i == j:
            print("*")
        else:
            print(" ", end=" ")
