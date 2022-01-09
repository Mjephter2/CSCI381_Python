for i in range(1, 10):
    for j in range(1, 10):
        if j >= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    for j in range(8, 0, -1):
        if j >= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
