# Set Operations and Differences

# Creating two sets for demonstration
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference of sets
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (elements in set_a but not in set_b):", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b (elements in either set_a or set_b but not both):", symmetric_difference_set)

# Comparing sets with other data types
# Sets are unordered and do not allow duplicates
example_set = {1, 2, 2, 3}
print("\nSet (duplicates removed):", example_set)

# Lists are ordered and allow duplicates
example_list = [1, 2, 2, 3]
print("List (duplicates allowed):", example_list)

# Tuples are ordered and immutable
example_tuple = (1, 2, 3)
print("Tuple (ordered and immutable):", example_tuple)

# Demonstrating the difference between mutable and immutable types
# Sets are mutable
mutable_set = {1, 2, 3}
print("\nOriginal mutable set:", mutable_set)
mutable_set.add(4)
print("Mutable set after modification:", mutable_set)

# Tuples are immutable
immutable_tuple = (1, 2, 3)
print("\nImmutable tuple:", immutable_tuple)
# Uncommenting the following line will raise a TypeError:
# immutable_tuple[0] = 10
