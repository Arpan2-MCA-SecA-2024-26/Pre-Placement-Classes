n=int(input("enter the number: "))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(end=" ")
    for j in range(1,2*i-1+1):
        print("*",end="")
    print("")