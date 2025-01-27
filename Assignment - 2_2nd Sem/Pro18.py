//18. Find the nth term a,b,b,c,c,c,……………………

def find_nth_term(n):
    i = 1
    count = 0
    while True:
        count += i
        if count >= n:
            return chr(96 + i)
        i += 1
n = int(input("Enter the nth term: "))
print(f"The {n}th term in the sequence is: {find_nth_term(n)}")