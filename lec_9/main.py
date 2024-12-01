import random

class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = [[random.randint(1, 100) for _ in range(col)]for _ in range(row)]
        
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrixes must have the same sizes.")
        result = Matrix(self.row, self.col)
        result.matrix = [[self[i][j] + other[i][j] for j in range(self.col)]for i in range(self.row)]
        
        return result
    
    def __sub__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrixes must have the same sizes.")
        result = Matrix(self.row, self.col)
        result.matrix = [[self[i][j] - other[i][j] for j in range(self.col)]for i in range(self.row)]
        
        return result
    
    def __mul__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrixes must have the same sizes.")
        result = Matrix(self.row, self.col)
        result.matrix = [[self[i][j] * other[i][j] for j in range(self.col)]for i in range(self.row)]
    
    
row1 = int(input("Enter number of rows for the first matrix: "))
col1 = int(input("Enter number of columns for the first matrix: "))

row2 = int(input("Enter number of rows for the second matrix: "))
col2 = int(input("Enter number of columns for the second matrix: "))

matrix1 = Matrix(row1, col1)
matrix2 = Matrix(row2, col2)

while True:
    try:
        print("Available operations!")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Exit")
        
        choose = input("Choose an operation (1-4): ")
        
        if choose == '4':
            print('Exiting operations')
            break
        
        if choose not in ['1', '2', '3']:
            print('Invalid operation, select valid operation')
            continue

        print("Result is: ", end='')
        match choose:
            case '1':
                print(matrix1 + matrix2)
            case '2':
                print(matrix1 - matrix2)
            case '3':
                print(matrix1 * matrix2)
                
    except ValueError:
        print("Enter numeric value")