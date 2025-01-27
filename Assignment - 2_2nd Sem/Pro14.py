//14. Find the nth term 1,1,2,6,24,………………………………

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
def findnthterm(n):
    return factorial(n-1)
number=int(input("Enter the nth term: "))
print(f"The {number}th term in the series is",findnthterm(number))