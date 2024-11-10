from itertools import count

# infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

# print the first 7 elements of the infinite iterator
for i in range(7):
    print(next(infinite_iterator))
