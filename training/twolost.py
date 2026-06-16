#Given two lists, find common elements using sets (intersection).

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common = list(set(a).intersection(set(b)))

print(common)

#Answer:
# [3, 4, 5]