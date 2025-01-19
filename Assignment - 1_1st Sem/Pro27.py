//27. Calculate the average of numbers in a list using a program. 

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
avg = sum(numbers) / len(numbers)
print("The average of the numbers in the list is:", avg)