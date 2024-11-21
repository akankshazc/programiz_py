import itertools
# Program to flatten a nested list


def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(flatten_list(nested_list))

# using itertools
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = list(itertools.chain(*nested_list))
print(flat_list)
