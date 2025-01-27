//8. 1-x^2/2!+x^4/4!+…………………………………………….

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)
x=int(input("Enter the value of x: "))
n=int(input("Enter the number of terms: "))
sum=1
for i in range(2,n+1):
    if (i%2==0):
        sum-=pow(x,pow(2,i-1))/factorial(pow(2,i-1))
    else:
        sum+=pow(x,pow(2,i-1))/factorial(pow(2,i-1))
print("The sum of series is:",sum)