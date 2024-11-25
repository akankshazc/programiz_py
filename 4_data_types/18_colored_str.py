# Program to Print Colored Text to the Terminal

# Using ANSI escape codes
from termcolor import colored
print('\x1b[38;2;5;86;243m' + 'Akanksha' + '\x1b[0m')

# Using the termcolor module

print(colored('Akanksha', 'red'))
