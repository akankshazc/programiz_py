# Python program to swap two variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')

# swapping without creating temporary variable
x, y = y, x

print(f'The value of x after swapping: {x}')
print(f'The value of y after swapping: {y}')

# other ways to swap (for integers only)

# by addition and subtraction
x = x + y
y = x - y
x = x - y

# by multiplication and division
x = x * y
y = x / y
x = x / y

# XOR swap
x = x ^ y
y = x ^ y
x = x ^ y
