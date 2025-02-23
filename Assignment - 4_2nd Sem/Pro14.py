#14. Intersection of two lists.

lst1 = list(map(int, input("Enter first list elements: ").split()))
lst2 = list(map(int, input("Enter second list elements: ").split()))
result = [num for num in lst1 if num in lst2]
print("Intersection:", result)