import random
n = 3

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
        
def matrix_mult(m1, m2, size):
    result = []

    for i in range(size):
        result.append(size * [0])

    for i in range(size):
        for j in range(size):
            result[i][j] = dot_product(get_row1(m1, i), get_col(m2, j), size)
    return result

def get_row1(m, row):
    return [ m[row][j] for j in range(len(m))]

# def get_row2(m, i):
#     return m[i]

def get_col(m, col):
    return [ m[i][col] for i in range(len(m))]

def dot_product(m1, m2, size):
    return sum([ m1[i]*m2[i] for i in range(size) ])


print("matrix1 ->")
print_matrix(matrix1, n)
print("matrix2 ->")
print_matrix(matrix2, n)
print("product ->")
print_matrix(matrix_mult(matrix1, matrix2, n), n)

    