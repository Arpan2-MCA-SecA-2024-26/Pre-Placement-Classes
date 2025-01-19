//14. Write a program to check if a string is a palindrome. 

st = input("Enter a string: ").lower().replace(" ", "")
if (st == st[::-1]):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")