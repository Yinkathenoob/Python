#Calculator
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
    }

def calculator():
    num1 = float(input('What is the first number?'))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the second number?'))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f'{num1}{operation_symbol}{num2} = {answer}')
        print(
f'''Type 'y'to contnue calculating with {answer},
Type 'r' to start a new calculation,
Type 'n' to end the program''')
        decide = input()
        if decide == 'y':
            num1 = answer
        elif decide == 'r':
            should_continue = False
            calculator()
        elif decide == 'n':
            should_continue = False


calculator()
