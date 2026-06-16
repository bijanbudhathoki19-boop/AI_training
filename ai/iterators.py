# Working with Iterators

# Sample list for the iterator example
list_example = [10, 20, 30]

# Creating an iterator from a list
list_iterator = iter(list_example)  # Using the iter() function to create an iterator
print("Iterator created from list:", list_iterator)

# Accessing elements using the next() function
print("First element:", next(list_iterator))  # Access the first element
print("Second element:", next(list_iterator))  # Access the second element
print("Third element:", next(list_iterator))  # Access the third element

# Using a for loop to iterate through the remaining elements
print("Remaining elements:")
for item in list_iterator:
    print(item)  # Print each remaining element in the iterator

# Demonstrating StopIteration exception
try:
    print("Attempting to access beyond the iterator:")
    print(next(list_iterator))  # This will raise StopIteration as the iterator is exhausted
except StopIteration:
    print("StopIteration exception raised: Iterator is exhausted.")