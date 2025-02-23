#8. Interchange first and last elements in a list.

lst = list(map(int, input("Enter list elements: ").split()))
first = lst[0]
last = lst[-1]
lst[0] = last
lst[-1] = first
print("Modified list:", lst)