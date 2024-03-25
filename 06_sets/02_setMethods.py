# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of two sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference between two sets
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)

# Symmetric difference between two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_difference_set)

# Check if a set is a subset of another set
subset_check = set1.issubset(set2)
print("Is set1 a subset of set2?", subset_check)

# Check if a set is a superset of another set
superset_check = set1.issuperset(set2)
print("Is set1 a superset of set2?", superset_check)

# Add an element to a set
set1.add(6)
print("After adding element to set1:", set1)

# Remove an element from a set
set1.remove(3)
print("After removing element from set1:", set1)

# Clear a set
set1.clear()
print("After clearing set1:", set1)