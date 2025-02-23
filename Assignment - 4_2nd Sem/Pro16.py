#16. Maximum and minimum element’s position in a list.

lst = list(map(int, input("Enter list elements: ").split()))
max_pos = lst.index(max(lst))
min_pos = lst.index(min(lst))
print("Max position:", max_pos)
print("Min position:", min_pos)