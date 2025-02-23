#11. Remove multiple elements from a list.

lst = list(map(int, input("Enter list elements: ").split()))
remove_lst = list(map(int, input("Enter elements to remove:
").split()))
for num in remove_lst:
 while num in lst:
 lst.remove(num)
print("Modified list:", lst)