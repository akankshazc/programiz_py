# Program for character count in a string

# get the string from the user
str1 = input("Enter a string: ")

# create a dictionary to store the character count
char_count = {}

# calculate the character count
for char in str1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# print the character count
for char, count in char_count.items():
    print(f"{char}: {count}")
