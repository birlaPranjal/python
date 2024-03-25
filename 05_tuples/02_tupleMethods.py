# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Count the number of occurrences of a value in the tuple
count = my_tuple.count(3)
print("Count:", count)

# Find the index of the first occurrence of a value in the tuple
index = my_tuple.index(4)
print("Index:", index)

# Concatenate two tuples
other_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + other_tuple
print("Concatenated Tuple:", concatenated_tuple)

# Get the length of the tuple
length = len(my_tuple)
print("Length:", length)

# Check if a value is present in the tuple
is_present = 5 in my_tuple
print("Is Present:", is_present)

# Get the maximum value in the tuple
maximum = max(my_tuple)
print("Maximum:", maximum)

# Get the minimum value in the tuple
minimum = min(my_tuple)
print("Minimum:", minimum)

# Convert the tuple to a list
my_list = list(my_tuple)
print("List:", my_list)

# Convert the list back to a tuple
new_tuple = tuple(my_list)
print("New Tuple:", new_tuple)