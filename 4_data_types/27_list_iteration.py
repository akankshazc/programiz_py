# Program to iterate through two lists in parallel

# List of names
names = ['John', 'Paul', 'George', 'Ringo']

# List of instruments
instruments = ['guitar', 'bass', 'guitar', 'drums']

# Iterate through the lists in parallel
for name, instrument in zip(names, instruments):
    print(name, 'plays', instrument)
