import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(x)

def calculator():
    print("Advanced Calculator\n")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")

    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        return

    if choice in ('1', '2', '3', '4', '5', '6'):
        x = float(input("Enter first number: "))

        if choice != '6':
            y = float(input("Enter second number: "))

        if choice == '1':
            result = add(x, y)
            print(f"{x} + {y} = {result}")
        elif choice == '2':
            result = subtract(x, y)
            print(f"{x} - {y} = {result}")
        elif choice == '3':
            result = multiply(x, y)
            print(f"{x} * {y} = {result}")
        elif choice == '4':
            result = divide(x, y)
            print(f"{x} / {y} = {result}")
        elif choice == '5':
            result = power(x, y)
            print(f"{x} ** {y} = {result}")
        elif choice == '6':
            result = square_root(x)
            print(f"Square root of {x} = {result}")

    else:
        print("Invalid input. Please enter a number between 0 and 6.")

    calculator()

# Run the calculator
calculator()
