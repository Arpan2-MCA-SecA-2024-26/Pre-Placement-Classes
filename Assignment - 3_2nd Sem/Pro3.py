//3. Write a program to input a 10 digit number and print alternate digits.

num = input("Enter a 10-digit number: ")
alternate_digits = num[::2]
print(f"Alternate digits: {alternate_digits}")