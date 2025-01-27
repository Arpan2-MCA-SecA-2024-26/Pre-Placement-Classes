//2. 1/1!+2/2!+3/3!+…………+n/n!

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
num=int(input("Enter the value of n: "))
result=0
for i in range(1,num+1):
    result+=i/factorial(i)
print(result)