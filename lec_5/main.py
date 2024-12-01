def sum_of_elements(list, exclude_negative = False):
    
    if exclude_negative:
        return sum(num for num in list if num > 0)
    else:
        return sum(list)

user_input = input('Input list of numbers separated by spaces: ')
numbers_list = list(map(int, user_input.split()))

choose = input("Do you want to exlude negative numbers? (y/n): ").lower()
choose = choose == 'y'

print(f"Result is: {sum_of_elements(numbers_list, choose)}")