# Accessing elements in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Updating elements in a tuple
my_tuple = (1, 2, 3)
updated_tuple = my_tuple[:2] + (4,) + my_tuple[2+1:]
print(updated_tuple)  # Output: (1, 2, 4)

# Unpacking a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print(joined_tuple)  # Output: (1, 2, 3, 4, 5, 6)