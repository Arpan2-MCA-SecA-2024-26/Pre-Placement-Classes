#15. Check if two lists are identical.

lst1 = list(map(int, input("Enter first list elements: ").split()))
lst2 = list(map(int, input("Enter second list elements: ").split()))
if lst1 == lst2:
 print("Identical")
else:
 print("Not Identical")