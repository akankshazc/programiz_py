# Program to represent enum

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# print the enum member
print(Color.RED)

# print the type of enum member
print(type(Color.RED))

# print the name of enum member
print(Color.RED.name)

# print the value of enum member
print(Color.RED.value)
