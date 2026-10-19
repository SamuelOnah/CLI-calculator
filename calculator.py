def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not Allowed."
        return a / b

print("Addition:")
print(add(10,5))
print(add(-3,8))
print(add(-5,-2))

print("\nSubtraction")
print(subtract(10,5))
print(subtract(3,8))


print("\nMultiplication")
print(multiply(4,3))
print(multiply(-4,3))
print(multiply(-4,-3))


