//5. Write a program to find the largest among three numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1 >= num2 and num1 >= num3):
    lar = num1
elif (num2 >= num1 and num2 >= num3):
    lar = num2
else:
    lar = num3
print("The largest number is:", lar)