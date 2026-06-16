#Write a function that returns multiple values (as a tuple) and show how to unpack them.

def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result   # returns a tuple

# Function call
result = calculate(10, 5)

print(result)
print(type(result))

## Unpacking the returned tuple


add, subtract = calculate(10, 5)

print("Addition:", add)
print("Subtraction:", subtract)