import random

class Matrix:
    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)]for _ in range(n)]
        
    def print(self):
        for row in self.matrix:
            print(row)
            
    def mean(self):
        return sum(sum(row) for row in self.matrix) / (self.__m * self.__n)
    
    def sum_of_row(self, index):
        return sum(self.matrix[index]) if 0 <= index < self.__n else IndexError("Index is out of range.")
    
    def avg_col(self, index):
        return (sum(row[index] for row in self.matrix) / self.__m) if 0 <= index < self.__m else IndexError("Index is out of range.")
    
    def print_submatrix(self, row1, row2, col1, col2):
        if 0 <= row1 <= row2 < self.__n and 0 <= col1 <= col2 < self.__m:
            for i in range(row1, row2 + 1):
                print(self.matrix[i][col1:col2 + 1])
        else:
            raise IndexError("Index is out of range.")

n = int(input("Enter number of rows for matrix: "))
m = int(input("Enter number of columns for matrix: "))

matrix = Matrix(n, m)

print("Matrix:")
matrix.print()

print(f"Matrix mean is: {matrix.mean()}")

row_index = input("Enter the index of row to sum: ")
print(f"Result is: {matrix.sum_of_row(row_index)}")

col_index = input("Enter the index of column to count the avg: ")
print(f"Result is: {matrix.avg_col(col_index)}")

row1 = input("Enter the start row index of submatrix: ")
row2 = input("Enter the end row index of submatrix:")
col1 = input("Enter the start column index of submatrix: ")
col2 = input("Enter the end column index of submatrix: ")

print("Submatrix is: ")
matrix.print_submatrix(row1, row2, col1, col2)