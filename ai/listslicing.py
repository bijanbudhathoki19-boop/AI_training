# List Slicing
# Definition:
# Slicing is used to extract a portion (sub-list) of a list
# using start, stop, and step values.

# Syntax:
# list_name[start:stop:step]

# start -> Index to begin from (inclusive)
# stop  -> Index to end at (exclusive)
# step  -> Number of positions to move

# When to use:
# 1. To extract a range of elements from a list.
# 2. To copy a list.
# 3. To reverse a list.
# 4. To skip elements using a step value.

# When NOT to use:
# 1. When you need only one element (use indexing).
# 2. When working with very large lists and memory is a concern.
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:6])

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[:4])
print(numbers[::2])