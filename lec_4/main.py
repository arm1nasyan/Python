def classify_numbers(list):
    odd_list = []
    even_list = []
    
    for item in list:
        if item % 2:
            odd_list.append(item)
        else:
            even_list.append(item)
            
    return even_list, odd_list

user_input = input('Input list of numbers separated by spaces: ')
numbers_list = list(map(int, user_input.split()))

evens, odds = classify_numbers(numbers_list)

print(f'Even numbers: {evens}')
print(f'Odd numbers: {odds}')