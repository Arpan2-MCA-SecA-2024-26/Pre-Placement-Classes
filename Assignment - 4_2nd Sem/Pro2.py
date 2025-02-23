#2. Reverse words in a given string.

string = input("Enter a string: ")
words = string.split()
result = " ".join(words[::-1])
print("Reversed words:", result)