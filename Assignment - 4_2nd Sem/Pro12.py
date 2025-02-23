#12. Remove duplicates from a list.

lst = list(map(int, input("Enter list elements: ").split()))
unique_lst = []
for num in lst:
 if num not in unique_lst:
 unique_lst.append(num)
print("List without duplicates:", unique_lst)