# Program to Randomly Select an Element From the List

import random


def random_element(lst):
    return random.choice(lst)


# Test the function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(random_element(my_list))
