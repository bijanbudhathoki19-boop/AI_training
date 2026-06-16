# Python Syntax Overview

# # Indentation in Python
# # Python uses indentation to define blocks of code. Indentation is mandatory and replaces braces used in other languages.
# for i in range(3):  # Loop starts here
#     print(f"Iteration {i}")  # Indented block

# # Comments in Python
# # Single-line comments start with a hash (#).
# # Multi-line comments can be written using triple quotes.
# """
# This is a multi-line comment.
# It spans multiple lines.
# """

# # Basic structure of a Python program
# # A Python program typically includes imports, function definitions, and the main execution block.

# Importing a module
import math

# Defining a function
def calculate_circle_area(radius:int):
    """Calculate the area of a circle given its radius."""
    return radius

# Main execution block
if __name__ == "__main__":
    radius = "hi"
    area = calculate_circle_area(radius)
    print(area)
    # print(f"The area of a circle with radius {radius} is {area:.2f}")
# Functions in Python
def greet_user(name):
    """Function to greet a user."""
    return f"Hello, {name}!"

# Example usage of the function
user_name = "Alice"
print(greet_user(user_name))

# Loops in Python
# For loop example
print("For loop example:")
for num in range(1, 6):  # Loop through numbers 1 to 5
    print(f"Number: {num}")

# While loop example
print("\nWhile loop example:")
counter = 1
while counter <= 5:  # Loop until counter exceeds 5
    print(f"Counter: {counter}")
    counter += 1

# Conditional Statements in Python
def check_number_sign(number):
    """Check if a number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage of conditional statements
test_number = -10
print(f"The number {test_number} is {check_number_sign(test_number)}.")
