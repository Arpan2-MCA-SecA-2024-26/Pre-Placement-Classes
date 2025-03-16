# 8. Write a Python program that converts the tuple (10, 20, 30, 40, 50) into a list, modifies the second element to 25, and then converts it back to a tuple.

my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
my_list[1] = 25
modified_tuple = tuple(my_list)
print("Modified tuple:", modified_tuple)