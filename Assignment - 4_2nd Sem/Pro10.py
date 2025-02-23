#10. Count occurrences of elements in a list.

lst = list(map(int, input("Enter list elements: ").split()))
element = int(input("Enter element to count: "))
count = lst.count(element)
print("Count:", count)