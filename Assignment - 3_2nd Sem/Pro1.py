#1. Write a program to input a 4 digit number and print the even and odd digits and total even and odd digits.

num = input("Enter a 4-digit number: ")
even_digits = [int(digit) for digit in num if int(digit) % 2 == 0]
odd_digits = [int(digit) for digit in num if int(digit) % 2 != 0]
print(f"Even digits: {even_digits}, Total even digits: {len(even_digits)}")
print(f"Odd digits: {odd_digits}, Total odd digits: {len(odd_digits)}")
