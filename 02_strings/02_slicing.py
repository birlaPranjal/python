# Slicing examples

# Slicing from the start to the end
string = "Hello, World!"
print("Original string:", string)
print("Sliced string from start to end:", string[:])

# Slicing from a specific index to the end
print("Sliced string from index 7 to end:", string[7:])

# Slicing from the start to a specific index
print("Sliced string from start to index 5:", string[:5])

# Slicing with negative indices
print("Sliced string from index -6 to -1:", string[-6:-1])

# Slicing with step size
print("Sliced string with step size 2:", string[::2])

# Slicing with negative step size
print("Sliced string with negative step size:", string[::-1])