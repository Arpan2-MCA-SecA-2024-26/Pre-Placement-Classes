//8. Write a program to input a number and search in a list using binary search.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = sorted([int(x) for x in input("Enter a sorted list of numbers: ").split()])
target = int(input("Enter the number to search: "))
index = binary_search(arr, target)
print(f"Number found at index {index}" if index != -1 else "Number not found.")
