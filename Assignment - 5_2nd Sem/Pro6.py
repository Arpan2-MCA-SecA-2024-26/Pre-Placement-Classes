# 6. Given two tuples:
# t1 = (1, 2, 3)
# t2 = (‘a’, ‘b’, ‘c’)
# Write a Python program to concatenate t1 and t2, then repeat the resulting tuple 2 times.

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
ct = t1 + t2
rt = ct * 2
print("Concatenated and repeated tuple:", rt)