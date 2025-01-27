//13. Find the nth term 14,28,20,40,…………………………….

def find_nth_term(n):
    if n % 2 !=0:
        term = 14 +(n//2)*6
    else:
        term = 28+((n//2)-1)*12
    return term
n = int(input("Enter the nth term: "))
print(f"The {n}th term of the sequence is: {find_nth_term(n)}")