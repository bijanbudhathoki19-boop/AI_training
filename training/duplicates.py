#Remove duplicates from a list using a set, then convert back to list preserving order? (Note: sets don't preserve order in older Python).

a = [1, 2, 3, 2, 4, 1, 5]

seen = set()
result = []

for item in a:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)