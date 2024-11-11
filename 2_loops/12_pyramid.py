# Program to print a pyramid

rows = int(input("Enter number of rows: "))

# function to print half pyramid using *


def star_pyramid(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()


star_pyramid(rows)

# function to print half pyramid using numbers


def number_pyramid(rows):
    num = 1
    for i in range(0, rows):
        num = 1
        for j in range(0, i + 1):
            print(num, end=' ')
            num = num + 1
        print()


number_pyramid(rows)

# function to print half pyramid using alphabets


def alphabet_pyramid(rows):
    ascii_value = 65
    for i in range(0, rows):
        ascii_value = 65
        for j in range(0, i + 1):
            character = chr(ascii_value)
            print(character, end=' ')
            ascii_value = ascii_value + 1
        print()


alphabet_pyramid(rows)

# function to print inverted half pyramid using *


def star_pyramid_inv(rows):
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=' ')
        print()


star_pyramid_inv(rows)

# function to print inverted half pyramid using numbers


def number_pyramid_inv(rows):
    num = 1
    for i in range(rows, 0, -1):
        num = 1
        for j in range(0, i):
            print(num, end=' ')
            num = num + 1
        print()


number_pyramid_inv(rows)

# function to print full pyramid using *


def star_pyramid_full(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=' ')
        print()


star_pyramid_full(rows)
