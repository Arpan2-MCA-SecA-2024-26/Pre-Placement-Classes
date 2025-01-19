//8. Write a program that swaps the values of two variables.

a = input("Enter the first variable (a): ")
b = input("Enter the second variable (b): ")
a, b = b, a
print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")