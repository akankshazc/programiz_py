# Python program to merge two dictionaries

X = {'a': 1, 'b': 2}
Y = {'b': 3, 'c': 4}

# In Python 3.5 or greater, you can use ** to merge two dictionaries
Z = {**X, **Y}
print(Z)

# In Python 3.9 and later versions, the | operator can be used to merge dictionaries.
Z = X | Y
print(Z)
