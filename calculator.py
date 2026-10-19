
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


operator = input("Choose an operation (+, -, *, /): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/":
    print(divide(num1, num2))
else:
    print("Unsupported operation.")
