# Define a list
my_list = [1, 2, 3, 4, 5]

# Accessing items by index
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Accessing items using negative index
print(my_list[-1])  # Output: 5
print(my_list[-3])  # Output: 3

# Accessing items using slicing
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[2:])   # Output: [3, 4, 5]

# Adding items to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.insert(2, 7)
print(my_list)  # Output: [1, 2, 7, 3, 4, 5, 6]

# Removing items from the list
my_list.remove(3)
print(my_list)  # Output: [1, 2, 7, 4, 5, 6]

del my_list[0]
print(my_list)  # Output: [2, 7, 4, 5, 6]

# Reversing the list
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 7, 2]               