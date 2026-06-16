# List Indexing
# Definition:
# List indexing is used to access individual elements
# of a list using their position (index).

# Syntax:
# list_name[index]

# Indexing starts from 0.
# Negative indexing starts from -1 (from the end).

# When to use:
# 1. To access a specific element in a list.
# 2. To update an element at a particular position.
# 3. To retrieve the first, last, or nth element.

# When NOT to use:
# 1. When you need multiple elements (use slicing).
# 2. When you don't know the position (use loops/search).
fruits = ["apple", "banana", "orange", "mango","pappaya"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange
print(fruits[3])  # mango
print(fruits[4])
fruits = ["apple", "banana", "orange", "mango"]

print(fruits[-1])  # mango
print(fruits[-2])  # orange
print(fruits[-3])  # banana
print(fruits[-4])  # apple