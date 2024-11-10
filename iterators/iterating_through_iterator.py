# define a list
my_list = [4, 7, 0, 6]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0

# get the fourth element of the iterator
print(next(iterator))  # prints 6

# getting the StopeIteration Exception
print(next(iterator))  # gives StopIteration error
