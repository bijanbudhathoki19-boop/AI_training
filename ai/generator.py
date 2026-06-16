# Creating and Using Generators

# Defining a generator function
def square_numbers(numbers):
    for number in numbers:
        yield number ** 2  # Yield the square of each number

# Using the generator function
numbers = [1, 2, 3, 4, 5]  # A list of numbers
squares = square_numbers(numbers)  # Create a generator object
print("Squares generated using generator function:")
for square in squares:
    print(square)  # Print each square generated

# Demonstrating generator expressions
cube_numbers = (number ** 3 for number in numbers)  # A generator expression to calculate cubes
print("Cubes generated using generator expression:")
for cube in cube_numbers:
    print(cube)  # Print each cube generated

# Comparing memory usage of a generator and a list
import sys

large_list = [i for i in range(1000)]  # A list comprehension
large_generator = (i for i in range(1000))  # A generator expression

print("Memory usage of list comprehension:", sys.getsizeof(large_list), "bytes")
print("Memory usage of generator expression:", sys.getsizeof(large_generator), "bytes")