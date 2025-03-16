# 10. Given the nested tuple: nested_tuple = ((1, 2, 3), (“a”, “b”, “c”), (True, False))
# Write a Python program to: Print the second element of the second inner tuple and Extract the last element of the third inner tuple.

nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
print("Second element of the second inner tuple:", nested_tuple[1][1])
last_element_of_third = nested_tuple[2][-1]
print("Last element of the third inner tuple:", last_element_of_third)