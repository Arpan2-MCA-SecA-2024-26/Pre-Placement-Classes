//10. Write a program to input a list of numbers and sort using insertion sort.

arr = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(f"Sorted list: {arr}")