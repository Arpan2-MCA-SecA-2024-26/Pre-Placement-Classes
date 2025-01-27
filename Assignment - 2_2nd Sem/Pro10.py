//10. Find the nth term 2,4,3,4,15,…………………………

def seriesterm(n):
    if n==1:
        return 2
    elif n%2==0:
        return 4
    else:
        return n*(n-2)
term=int(input("Enter the nth term: "))
nthterm=seriesterm(term)
print(f"The {term}th term of the series is",nthterm)