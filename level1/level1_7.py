string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("True (The strings are anagrams)")
else:
    print("False (The strings are not anagrams)")
