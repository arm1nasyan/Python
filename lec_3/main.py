def calculator():
    print('Available operations!')
    print('1. Addition (+)')
    print('2. Subtraction (-)')
    print('3. Multiplication (*)')
    print('4. Division (/)')
    print('5. Exit')
    
    while True:
        try:
            choose = input('Choose an operation (1-5):')
            
            if choose == '5':
                print("Exiting calculator")
                break
            
            if choose not in ['1', '2', '3', '4']:
                print('Invalid operation, select valid operation')
                continue
            
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            
            print('Result is: ', end='')
            match choose:
                case '1':
                    print(num1 + num2)
                case '2':
                    print(num1 - num2)
                case '3':
                    print(num1 * num2)
                case '4':
                    if num2 == '0':
                        print("Invalid input, number can't be divided by 0")
                    else:
                        print(num1 / num2)
        except ValueError:
            print('Enter numeric value')
            
calculator()