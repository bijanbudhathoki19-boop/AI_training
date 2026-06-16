#Write a function to find if all elements in a list are unique using a set.

def all_unique(lst):
    return len(lst) == len(set(lst))

# Example
a = [1, 2, 3, 4, 5]
b = [1, 2, 2, 3, 4]

print(all_unique(a))
print(all_unique(b))