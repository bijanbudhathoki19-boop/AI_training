#Count the frequency of each element in a list using only built-in methods (no Counter)

my_list = [1, 2, 1, 3, 2, 1, 4, 3]

frequency = {}

for item in my_list:
    frequency[item] = my_list.count(item)

print(frequency)

#Answer:
# {1: 3, 2: 2, 3: 2, 4: 1}