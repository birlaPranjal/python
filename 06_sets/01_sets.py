# Create a set
my_set = {1, 2, 3, 4, 5}

# Access set items
for item in my_set:
    print(item)

# Add items to the set
my_set.add(6)
my_set.update([7, 8, 9])

# Remove items from the set
my_set.remove(3)
my_set.discard(4)

# Print the updated set
print(my_set)

# Create another set
other_set = {4, 5, 6, 7, 8}

# Join two sets using union()
joined_set = my_set.union(other_set)

# Print the joined set
print(joined_set)