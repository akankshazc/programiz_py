# Returning multiple values from a function

# using a comma
def name():
    return "John", "Doe"


print(name())

name_1, name_2 = name()
print(name_1, name_2)

# using a dict


def name_2():
    return {"first": "John", "last": "Doe"}


print(name_2())
