# Program to remove punctuation from a given string

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""

for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char