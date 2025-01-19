//15. Calculate the factorial of a number using both iterative and recursive approaches in separate programs.
//a. Iterative approach

def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
if (num < 0):
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {fact_iterative(num)}")