##Create a tuple from a list and demonstrate why tuples are immutable. Try to modify an element and handle the error.


# Create a list
my_list = [10, 20, 30, 40]

# Convert list to tuple
my_tuple = tuple(my_list)

print("Tuple:", my_tuple)

# Try to modify an element of the tuple
try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error:", e)

print("Tuple after modification attempt:", my_tuple)

##Answer
# Tuple: (10, 20, 30, 40)
# Error: 'tuple' object does not support item assignment
# Tuple after modification attempt: (10, 20, 30, 40)