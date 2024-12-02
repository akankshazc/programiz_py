# Program to check if two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# convert strings to lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is the same:
if len(str1) != len(str2):
    print("Strings are not anagrams")
    exit()

# sort the strings
str1 = sorted(str1)
str2 = sorted(str2)

# if sorted strings are equal, then they are anagrams
if str1 == str2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
