//4. 1+x+x^2+x^3+……………………………………+x^n

x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
result=1
for i in range(1,n+1):
    result+=pow(x,i)
print(result)