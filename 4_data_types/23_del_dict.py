# Program to delete an element from the dictionary

# using del keyword

# create a dictionary
my_dict = {
    'name': 'Jack',
    'age': 26,
    'profession': 'Developer'
}

# delete an element
del my_dict['profession']

print(my_dict)

# using pop() method

# create a dictionary
my_dict = {
    'name': 'Jack',
    'age': 26,
    'profession': 'Developer'
}

# delete an element

my_dict.pop('profession')

print(my_dict)
