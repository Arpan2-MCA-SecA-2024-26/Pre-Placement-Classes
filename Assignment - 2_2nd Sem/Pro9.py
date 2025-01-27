//9. 1+2+11+26+47+……………………………………………..

def isSeries(n):
    sum=1
    term=0
    for i in range(n):
        if(i==0 or i==1):
            sum=sum+term+i
            term+=1
        else:
            term+=3*(2*i-1)
            sum+=term
    return sum
num=int(input("Enter the number of terms: "))
result=isSeries(num)
print("The sum of series is:",result)