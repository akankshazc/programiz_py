# program to calculate all permutations of a string

# import the permutations function from the itertools module
from itertools import permutations

# get the string from the user
str1 = input("Enter a string: ")

# calculate all permutations of the string
perm = permutations(str1)

# print all permutations
for i in list(perm):
    print(''.join(i))
