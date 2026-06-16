# Dictionary Comprehension
# Definition:
# A concise and Pythonic way to create a new dictionary by
# iterating over an iterable and generating key-value pairs.

# Syntax:
# {key_expression: value_expression for item in iterable}

# When to use:
# 1. When you need to create a dictionary from another iterable.
# 2. When keys and values can be generated using simple expressions.
# 3. When transforming existing dictionary data.
# 4. When filtering dictionary entries based on a condition.
# 5. When you want cleaner and shorter code than a traditional loop.

# When NOT to use:
# 1. When the logic is complex and hard to understand.
# 2. When multiple nested conditions reduce readability.
# 3. When performing side effects instead of creating a dictionary.

# Example 1: Create a dictionary of numbers and their squares


numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}

print(squares)
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Example 2: Filter only even numbers
even_squares = {num: num ** 2 for num in numbers if num % 2 == 0}

print(even_squares)
# Output:
# {2: 4, 4: 16}


# Example 3: Convert values to uppercase
students = {
    "s1": "abinash",
    "s2": "sandip",
    "s3": "ram"
}

upper_students = {
    key: value.upper()
    for key, value in students.items()
}

print(upper_students)
# Output:
# {'s1': 'ABINASH', 's2': 'SANDIP', 's3': 'RAM'}