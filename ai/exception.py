try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
    try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"You entered: {num}")