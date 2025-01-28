//7. Write a program to input a number and search in a list using linear search.

arr = [int(x) for x in input("Enter a list of numbers: ").split()]
target = int(input("Enter the number to search: "))
if target in arr:
    print(f"Number found at index {arr.index(target)}")
else:
    print("Number not found.")