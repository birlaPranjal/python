# String methods demonstration

# 1. capitalize(): Converts the first character of the string to uppercase and the rest to lowercase
string = "hello world"
print(string.capitalize())

# 2. upper(): Converts all characters in the string to uppercase
print(string.upper())

# 3. lower(): Converts all characters in the string to lowercase
print(string.lower())

# 4. swapcase(): Swaps the case of each character in the string (lowercase to uppercase and vice versa)
print(string.swapcase())

# 5. title(): Converts the first character of each word in the string to uppercase and the rest to lowercase
print(string.title())

# 6. count(): Returns the number of occurrences of a specified substring in the string
print(string.count("o"))

# 7. find(): Returns the index of the first occurrence of a specified substring in the string, or -1 if not found
print(string.find("world"))

# 8. index(): Returns the index of the first occurrence of a specified substring in the string, or raises an exception if not found
print(string.index("world"))

# 9. replace(): Replaces all occurrences of a specified substring with another substring in the string
print(string.replace("world", "universe"))

# 10. strip(): Removes leading and trailing whitespace characters from the string
string = "   hello   "
print(string.strip())

# 11. lstrip(): Removes leading whitespace characters from the string
print(string.lstrip())

# 12. rstrip(): Removes trailing whitespace characters from the string
print(string.rstrip())

# 13. split(): Splits the string into a list of substrings based on a specified delimiter (default is whitespace)
string = "hello world"
print(string.split())

# 14. join(): Joins the elements of a list into a single string, using the specified string as a separator
list_of_words = ["hello", "world"]
print(" ".join(list_of_words))

# 15. isalpha(): Returns True if all characters in the string are alphabetic (letters), False otherwise
print(string.isalpha())

# 16. isnumeric(): Returns True if all characters in the string are numeric (digits), False otherwise
number = "123"
print(number.isnumeric())

# 17. isdigit(): Returns True if all characters in the string are digits, False otherwise
print(number.isdigit())

# 18. islower(): Returns True if all characters in the string are lowercase, False otherwise
print(string.islower())

# 19. isupper(): Returns True if all characters in the string are uppercase, False otherwise
print(string.isupper())

# 20. startswith(): Returns True if the string starts with a specified substring, False otherwise
print(string.startswith("hello"))

# 21. endswith(): Returns True if the string ends with a specified substring, False otherwise
print(string.endswith("world"))