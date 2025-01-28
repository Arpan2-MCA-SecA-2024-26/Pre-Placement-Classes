//9. Write a program to input a list of numbers and sort using bubble sort.

arr = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f"Sorted list: {arr}")