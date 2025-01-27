//6. 1*2*3+2*3*4+……………………………….+n*(n+1)*(n+2)

n=int(input("Enter the value of n: "))
result=0
for i in range(1,n+1):
    result+=i*(i+1)*(i+2)
print("The sum of series is:",result)