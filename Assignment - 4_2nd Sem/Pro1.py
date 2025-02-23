#1. Removing all duplicates from a string.

string = input("Enter a string: ")
result = ""
for char in string:
 if char not in result:
 result += char
print("String without duplicates:", result)