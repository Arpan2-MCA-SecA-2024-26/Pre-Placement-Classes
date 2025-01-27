//12. Find the nth term 0,0,2,1,4,2,6,3,8……………………….

def findnthterm(n):
    if (n%2==0):
        return (n-1)//2
    else:
        return (n-1)
Number=int(input("Enter the nth term: "))
print(f"The {Number}th term of the series is {findnthterm(Number)}")