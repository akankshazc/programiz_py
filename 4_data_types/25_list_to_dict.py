# Program to convert two lists into a dictionary

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

# Method 1: Using the zip() function
person = dict(zip(keys, values))

print(person)

# Method 2: Using a dictionary comprehension
person = {keys[i]: values[i] for i in range(len(keys))}

print(person)

# Method 3: Using the fromkeys() method
person = dict.fromkeys(keys, None)

for i, key in enumerate(keys):
    person[key] = values[i]

print(person)
