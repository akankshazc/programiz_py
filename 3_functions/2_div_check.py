# Python program to find given list of numbers divisible by number

# Make a list of numbers
my_list = [34, 25, 65, 74, 33, 98, 453]

div_by = int(input("Enter a number to divide by: "))

# use lambda function to filter
result = list(filter(lambda x: (x % div_by == 0), my_list))

print("Numbers divisible by", div_by, "are", result)
