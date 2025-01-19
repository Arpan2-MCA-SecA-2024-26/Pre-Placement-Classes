//26. Write a Python program to find the LCM (Least Common Multiple) of two numbers. 

import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = abs(num1 * num2) // math.gcd(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")