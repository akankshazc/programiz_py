import cmath

# python program to calculate the square root

# For positive numbers

# Input from the user
num = float(input('Enter a positive number: '))

num_sqrt = num ** 0.5
print("The square root of %0.3f is %0.3f" % (num, num_sqrt))


# For real or complex numbers

num = eval(input('Enter a complex number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+(2:0.3f)j'.format(num,
      num_sqrt.real, num_sqrt.imag))
