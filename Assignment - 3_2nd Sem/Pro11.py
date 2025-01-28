//11. Write a program to input a list of numbers and sort using selection sort.

arr = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(f"Sorted list: {arr}")