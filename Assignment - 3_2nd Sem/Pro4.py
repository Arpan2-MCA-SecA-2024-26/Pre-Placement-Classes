//4. Write a program, which will find all such numbers between 1000 and 3000 such that each digit of the number is an even number.

even_numbers = [num for num in range(1000, 3001) if all(int(digit) % 2 == 0 for digit in str(num))]
print(f"Numbers where all digits are even: {even_numbers}")