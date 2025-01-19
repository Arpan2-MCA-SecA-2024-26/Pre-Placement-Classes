//15. Calculate the factorial of a number using both iterative and recursive approaches in separate programs.
//b. Recursive approach

def fact_recursive(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact_recursive(n - 1)
num = int(input("Enter a number: "))
if (num < 0):
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {fact_recursive(num)}")