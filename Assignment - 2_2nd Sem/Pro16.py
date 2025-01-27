//16. Find the nth term 5,13,25,41,61,…………………….

def nth_term(n):
    return (2 * n**2 + 2 * n + 1)
n = int(input("Enter the nth term: "))
print(f"The {n}th term is: {nth_term(n)}")