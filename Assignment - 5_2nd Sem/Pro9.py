# 9. Write a function math_operations(a, b) that takes two numbers as input and returns a tuple containing their sum, difference, product, and quotient.

def math_operations(a, b):
 sum_result = a + b
 difference_result = a - b
 product_result = a * b
 quotient_result = a / b if b != 0 else None
 return (sum_result, difference_result, product_result, quotient_result)
a = 10
b = 5
result = math_operations(a, b)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])