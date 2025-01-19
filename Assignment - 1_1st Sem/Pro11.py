//11. Write a Python program to generate the Fibonacci sequence. 

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
if (n <= 0):
    print("Please enter a positive integer.")
elif (n == 1):
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b