def find_largest(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num          
    return largest


user_input = input("Enter numbers separated by spaces ( 3 41 56 21): ")

try:
    numbers_list = [float(x) for x in user_input.split()]
    result = find_largest(numbers_list)
    print(f"The largest number is: {result}")
    
except ValueError:
    print("Error: Please make sure you only enter numbers separated by spaces.")
