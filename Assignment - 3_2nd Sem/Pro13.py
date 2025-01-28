//13. Write a program to input a string and a number to encode the string by adding the number to every character in the string.

string = input("Enter a string: ")
shift = int(input("Enter a number: "))
encoded = ""
for char in string:
    ascii_value = ord(char)
    new_ascii_value = ascii_value + shift
    new_char = chr(new_ascii_value)
    encoded += new_char
print("Encoded string:", encoded)