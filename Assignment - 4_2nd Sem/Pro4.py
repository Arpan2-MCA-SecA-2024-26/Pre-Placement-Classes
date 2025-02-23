#4. Remove ith character from the string.

string = input("Enter a string: ")
i = int(input("Enter index to remove: "))
result = string[:i] + string[i+1:]
print("String after removal:", result)