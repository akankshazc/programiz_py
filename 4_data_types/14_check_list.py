# Program to check if a list is empty

def check_list(my_list):
    if not my_list:
        return "List is empty"
    else:
        return "List is not empty"


my_list = []
print(check_list(my_list))

my_list = [1, 2, 3]
print(check_list(my_list))
