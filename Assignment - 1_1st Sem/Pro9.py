//9. Calculate the square root of a number using Python.

import math
number = float(input("Enter a number: "))
if number < 0:
    print("Square root is not defined for negative numbers.")
else:
    sqrt = math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")