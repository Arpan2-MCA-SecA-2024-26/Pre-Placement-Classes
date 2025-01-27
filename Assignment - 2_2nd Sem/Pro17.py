//17. Find the nth term 0,6,0,12,0,90,…………………….

def nth_term(n):
    if n%2!=0:
        return 0
    else:
        if n==2 or n==4:
            return n*3
        else:
            return (n*3)*(n-1)
n = int(input("Enter the nth term: "))
print(f"The {n}th term is: {nth_term(n)}")