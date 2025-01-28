//12. Write a program to find the frequency of characters in a given string.

string = input("Enter a string: ")
frequency = {char: string.count(char) for char in set(string)}
print(f"Character frequencies: {frequency}")