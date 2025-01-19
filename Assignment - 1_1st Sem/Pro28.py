//28. Create a program that generates a multiplication table for a given number. 

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")