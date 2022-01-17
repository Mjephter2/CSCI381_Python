import random
n = 5

# declare matrices
matrix1 = []
matrix2 = []

# initialize matrices with zeros
for i in range(n):
    matrix1.append(n * [0])
    matrix2.append(n * [0])

# fill matrices with random values
for i in range(n):
    for j in range(n):
        matrix1[i][j] = random.randint(0, 10)
        matrix2[i][j] = random.randint(0, 10)


def print_matrix(m, size):
    for i in range(size):
        print("\t[", end='')
        for j in range(size):
            print(format(m[i][j], "3.0f"), "", end="")
        print("]")


print("matrix1 ->")
print_matrix(matrix1, n)
print("matrix2 ->")
print_matrix(matrix2, n)


def matrix_add(m1, m2, size):
    result = []
    for i in range(size):
        result.append(size * [0])
    for i in range(size):
        for j in range(size):
            result[i][j] = m1[i][j] + m2[i][j]
    return result


matrix_sum = matrix_add(matrix1, matrix2, n)

print("sum ->")
print_matrix(matrix_sum, n)


def matrix_mult(m1, m2, size):
    result = []

    for i in range(size):
        result.append(size * [0])

    for i in range(size):
        for j in range(size):
            product_cell = 0
            for p in range(0, size):
                product_cell += m1[i][p] * m2[p][j]
            result[i][j] = product_cell
    return result




matrix_p = matrix_mult(matrix1, matrix2, n)

print("product ->")
print_matrix(matrix_p, len(matrix_p))
