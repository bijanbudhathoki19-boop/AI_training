import copy

def show_copy():
    # Original nested list
    original = [[1, 2, 3], [4, 5, 6]]
    
    # Shallow Copy
    shallow = original.copy()          # or copy.copy(original)
    
    # Deep Copy
    deep = copy.deepcopy(original)
    
    print("Original :", original)
    
    # Modify nested list
    shallow[0][0] = 99
    
    print("After change:")
    print("Original :", original)   # ← Changed!
    print("Shallow   :", shallow)   # ← Changed!
    print("Deep      :", deep)      # ← Not changed!
show_copy()


# Shallow Copy:
# - Fast
# - Only top level is copied
# - Nested lists/dicts are shared (reference)
# - Changing nested value affects original

# Deep Copy:
# - Slower (copies everything recursively)
# - Fully independent copy
# - Changing anything in deep copy does NOT affect original