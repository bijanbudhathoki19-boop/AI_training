#Write code to rotate a list to the right by k positions. Example: `[1,2,3,4,5]` rotated by 2 becomes `[4,5,1,2,3]`.

def rotate_right(lst, k):
    k = k % len(lst)  # handle k > length
    return lst[-k:] + lst[:-k]

# Example
a = [1, 2, 3, 4, 5]
print(rotate_right(a, 2))

#Answer:
# [4, 5, 1, 2, 3]