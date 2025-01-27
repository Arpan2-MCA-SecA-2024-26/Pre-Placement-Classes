//7. 1-1/2+1/3-1/4+………………………………………………..

n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n+1):
    if (i%2==0):
        sum-=1/i
    else:
        sum+=1/i
print("The sum of series is:",sum)