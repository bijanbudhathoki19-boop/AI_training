# List Comprehension
# Definition:
# A concise and Pythonic way to create a new list by iterating
# over an iterable and optionally applying conditions.

# When to use:
# 1. When you need to create a new list from an existing iterable.
# 2. When the logic is simple and can be written in a single expression.
# 3. When you want shorter and more readable code than a traditional loop.
# 4. When filtering elements from a collection.
# 5. When transforming data (e.g., squaring numbers, converting text to uppercase).

# When NOT to use:
# 1. When the logic is complex and difficult to read in one line.
# 2. When multiple nested conditions make the code confusing.
# 3. When you are performing actions other than creating a list
#    (e.g., writing to a file, making API calls, logging).

# Example: Create a list of squares
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers] ## list vitra ko ma nei operation garni

print(squares)
# Output: [1, 4, 9, 16, 25]


# Example: Filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
# Output: [2, 4]


# Example: Transform strings to uppercase
names = ["abinash", "sandip", "ram"]

upper_names = [name.upper() for name in names]

print(upper_names)
# Output: ['ABINASH', 'SANDIP', 'RAM']


# for printing vowles
a = ["a", "d", "i", "o"]

vowels = [char for char in a if char in "aeiou"]

print(vowels)


## find odd number

numbers = [1, 2, 3, 4, 5]

odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)