# Program to remove duplicate elements from a list

list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# create a set from the list to remove duplicates
set1 = set(list1)

# convert the set back to a list
list1 = list(set1)

# print the list without duplicates
print(list1)
