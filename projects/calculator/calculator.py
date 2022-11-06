from art import logo

# Adding
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

calculator = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

def calculating():

    print(logo)

    num1 = float(input('What is the first number?: '))

    for option in calculator:
        print(option)

    end_program = True

    while end_program:

        symbol = input('Pick an operation from the line of above: ')

        num2 = float(input('What is the next number?: '))

        operation_function = calculator[symbol]
        answer = operation_function(num1,num2)

        print(f'{num1} {symbol} {num2} = {answer}')

        option = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to start over. Use other key to exit: ' )

        if option == 'y':
            num1 = answer
        elif option == 'n':
            end_program = False
            calculating()
        else:
            end_program = False

calculating()