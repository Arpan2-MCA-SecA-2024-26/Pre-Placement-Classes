//6. Given a sorted array of positive integers arr, and an integer n which represents the length of arr, the task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

arr = [int(x) for x in input("Enter a sorted array: ").split()]
result = []
while arr:
    if arr: result.append(arr.pop(-1))
    if arr: result.append(arr.pop(0))
print(f"Rearranged array: {result}")
