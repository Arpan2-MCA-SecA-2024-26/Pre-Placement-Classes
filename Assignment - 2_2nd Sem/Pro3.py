//3. 1/1^1+2/2^2+3/3^3+………………….+n/n^n

num=int(input("Enter the value of n: "))
result=0
for i in range(1,num+1):
    result+=i/pow(i,i)
print(result)