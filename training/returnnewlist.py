#Write a function that takes a list and returns a new list with duplicates removed while preserving the original order.

def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

# Example
a = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(a))