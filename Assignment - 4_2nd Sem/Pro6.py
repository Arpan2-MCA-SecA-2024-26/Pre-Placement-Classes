#6. Check Anagram string.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
sorted1 = sorted(string1)
sorted2 = sorted(string2)
if sorted1 == sorted2:
 print("Anagram")
else:
 print("Not an Anagram")