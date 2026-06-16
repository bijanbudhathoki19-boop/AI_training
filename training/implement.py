#Implement a function to find the second largest element in a list without sorting the entire list.

def second_largest(lst):
    if len(lst) < 2:
        return None

    largest = second = float('-inf')

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

# Example
a = [10, 5, 20, 8, 20]
print(second_largest(a))