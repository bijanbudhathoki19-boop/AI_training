# Lambda Function
# Definition:
# A lambda function is a small anonymous (nameless) function
# that can have any number of arguments but only one expression.

# Syntax:
# lambda arguments: expression

# When to use:
# 1. For short, simple functions used only once.
# 2. With map(), filter(), and reduce().
# 3. As a key function for sorting.
# 4. When defining a separate function would be unnecessary.

# When NOT to use:
# 1. When the logic is complex.
# 2. When multiple statements are required.
# 3. When readability becomes poor.

# Normal function
def square(x):
    return x ** 2

print(square(5))
# Output: 25

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))
# Output: 25

# Return two values
get_values = lambda x: (x, x ** 2)

result = get_values(5)

print(result)
# Output: (5, 25)

# Normal function
def square(x):
    return x ** 2

print(square(5))
# Output: 25

# Lambda equivalent
square = lambda x:(x,x ** 2)
                   


print(square(5))
# Output: 25
#multiple arguments pathauna tuple huna parxa
