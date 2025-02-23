#3. Print even length words in a string.

string = input("Enter a string: ")
words = string.split()
for word in words:
 if len(word) % 2 == 0:
 print(word)