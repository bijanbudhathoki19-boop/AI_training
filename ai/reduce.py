# reduce() Function
# Definition:
# reduce() repeatedly applies a function to items in an iterable
# and reduces them to a single value.

# Syntax:
# from functools import reduce
# reduce(function, iterable)

# When to use:
# 1. When you need a single result from multiple values.
# 2. For summation, multiplication, finding max/min, etc.
# 3. When performing cumulative operations.

# When NOT to use:
# 1. When built-in functions such as sum(), max(), min()
#    are clearer and simpler.
# 2. When the reduction logic is difficult to understand.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)

print(total)
# Output: 15