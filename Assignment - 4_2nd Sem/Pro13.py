#13. Find second largest number in a list.

lst = list(map(int, input("Enter list elements: ").split()))
lst = list(set(lst))
lst.sort()
print("Second largest number:", lst[-2])