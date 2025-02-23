#7. To replace all characters of a list except the given character.

string = input("Enter a string: ")
char = input("Enter character to keep: ")
result = ""
for c in string:
 if c == char:
 result += c
 else:
 result += "*"
print("Modified string:", result)