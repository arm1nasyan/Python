import random
import time

def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time for {function.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper

@time_decorator
def create_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            numbers = [str(random.randint(1, 100)) for _ in range(20)]
            file.write(" ".join(numbers) + '\n')

@time_decorator
def filter_rewrite(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    new_list = []
    for line in lines:
        numbers = list(map(int, line.split()))
        filtered = list(filter(lambda x: x > 40, numbers))
        new_list.append(" ".join(map(str, filtered)))
        
    with open(filename, 'w') as file:
        for line in new_list:
            file.write(line + "\n")

@time_decorator     
def read_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

filename = input("Enter filename: ")
create_file(filename)
filter_rewrite(filename)

generator = read_file_generator(filename)

for i, line in enumerate(generator):
    print(f"Line{i+1}: {line}")