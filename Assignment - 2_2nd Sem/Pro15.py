//15. Find the nth term 1,8,54,384,…………………………..

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
def nth_term(n):
    return pow(n,2)* factorial(n)
Number=int(input("Enter the nth term: "))
print(f"The {Number}th term of the series is {nth_term(Number)}")