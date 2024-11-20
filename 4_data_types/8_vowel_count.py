# Python program to count the number of each vowel

# string of vowels
vowels = 'aeiou'

# string input from user
ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1

print(count)
