//5. 1*3+3*5+………………………………………………….

n=int(input("Enter the number of terms: "))
result=0
for i in range(1,n+1):
    result+=(2*i-1)*(2*i+1)
print("The sum of series is: ",result)