//11. Find the nth term 3,5,33,35,53,……………………..

def find_nth_term(n):
    result= []
    seq= ["3", "5"]
    while n>len(result):
        current=seq.pop(0)
        result.append(current)
        seq.append(current+"3")
        seq.append(current+"5")
    return result[n-1]
n =int(input("Enter the nth term: "))
print(f"The {n}th term in the sequence is: {find_nth_term(n)}")