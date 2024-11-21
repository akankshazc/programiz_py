# Program to slice lists

my_list = [1, 2, 3, 4, 5]

print(my_list[1:4:2])

# function to create a new list from an existing list using list slicing.


def slice_list(my_list, start, end, step):
    return my_list[start:end:step]
