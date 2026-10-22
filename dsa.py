def find_largest(numbers):
    if not numbers:
        return list_number 

list_number = [3, 41, 56, 21, 76, 9]
        
numbers = input("choose your favourite numbers ")

while True:
    if numbers != list_number:
        print(f"{numbers} is the highest number in the room")
        break
    elif numbers != 20:
        print(f"The number you selected is {numbers}")
        break
    elif numbers != 10:
        print("Try a bigger number")
        break
    else:  
        print("76")

print(find_largest(list_number))