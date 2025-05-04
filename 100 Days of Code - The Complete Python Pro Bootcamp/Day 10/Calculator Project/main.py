import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Can't divide by zero!"
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)
choice = 'no'
result = 0

while True:

    if choice == 'no':
        f_number = float(input("What is the first number?: "))
    else:
        f_number = result

    for key in functions:
        print(key)

    operation = input("Pick an operation: ")
    while operation not in functions.keys():
        operation = input("Invalid operation - Pick an operation: ")

    s_number = float(input("What is the second number?: "))

    result = functions[operation](f_number, s_number)

    print(f"{f_number} {operation} {s_number} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
    while choice != "y" and choice != "n":
        choice = input("Please type 'y' or 'n")









