# Define the numbers
num1 = 10
num2 = 20

# Create a string with placeholders 
string = "The first number is {} and the second number is {}."

# Use the format() method to insert the numbers into the string

formatted_string = string.format(num1, num2)  

formatted_string2 = string.format(num2, num1)  

# Print the formatted strings
print(formatted_string)  
print(formatted_string2)  