#5. Check whether symmetrical/Palindrome string.

string = input("Enter a string: ")
reverse = string[::-1]
if string == reverse:
 print("Palindrome")
else:
 print("Not a Palindrome")