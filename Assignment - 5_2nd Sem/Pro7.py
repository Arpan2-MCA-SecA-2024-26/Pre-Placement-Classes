# 7. Write a function check_membership(t, element) that takes a tuple t and a value element as input and returns True if the element exists in the tuple, otherwise False.

def check_membership(t, element):
 return element in t
my_tuple = (1, 2, 3, 4, 5)
element_to_check = 3
print("Is the element in the tuple?", check_membership(my_tuple, element_to_check))