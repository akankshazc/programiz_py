# Program to sort a dictionary by value


def sort_dict_by_value(my_dict):
    sorted_dict = {k: v for k, v in sorted(
        my_dict.items(), key=lambda item: item[1])}
    return sorted_dict
