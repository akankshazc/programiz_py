# Program to Create a Long Multiline String

# Method 1: Using triple quotes
string = '''This is a long multiline string
that spans multiple lines
and is enclosed in triple quotes.'''

print(string)

# Method 2: Using parentheses
string = ('This is a long multiline string '
          'that spans multiple lines '
          'and is enclosed in parentheses.')

print(string)

# Method 3: Using backslashes
string = 'This is a long multiline string ' \
         'that spans multiple lines ' \
         'and is enclosed in backslashes.'

print(string)

# Method 4: Using the join() method

string = '\n'.join(['This is a long multiline string',
                    'that spans multiple lines',
                    'and is enclosed in a list.'])

print(string)

# Method 5: Using the + operator

string = 'This is a long multiline string ' + \
    'that spans multiple lines ' + \
    'and is enclosed in the + operator.'

print(string)
