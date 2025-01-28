//5. Write a program that prints a list where the values are square of numbers between 5000 and 7000 (both included).

squares = [num ** 2 for num in range(5000, 7001)]
print(f"Squares of numbers between 5000 and 7000: {squares}")