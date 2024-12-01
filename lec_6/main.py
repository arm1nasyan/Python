import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def get_column_sum(matrix, index):
    return sum(row[index] for row in matrix)

def get_row_average(matrix, index):
    return sum(matrix[index]) / len(matrix[index])

matrix = generate_random_matrix(3, 3)

print("Matrix:")
for row in matrix:
    print(row)
    
print(f"Column sum is: {get_column_sum(matrix, 0)}")
print(f"Row average is: {get_row_average(matrix, 0)}")