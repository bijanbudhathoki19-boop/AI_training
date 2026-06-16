# map() Function
# Definition:
# map() applies a function to every item in an iterable and
# returns a map object (iterator) containing the results.

# Syntax:
# map(function, iterable)

# When to use:
# 1. When the same operation must be applied to every element.
# 2. When you want to avoid writing explicit loops.
# 3. When a transformation function already exists.

# When NOT to use:
# 1. When the transformation logic is very simple.
#    (List comprehension is often more readable.)
# 2. When the operation has side effects instead of returning values.

# Example: Square each number

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
# Output: [1, 4, 9, 16, 25]