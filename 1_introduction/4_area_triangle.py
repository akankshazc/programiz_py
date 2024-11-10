# Python program to find the area of a triangle with sides a, b and c

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi perimeter
s = (a + b + c) / 2

# calculate the area (Heron's formula)
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
