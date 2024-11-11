# Python program to find the factorial of a number provided by the user

def factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Test the function
n = int(input("Enter a number: "))

print(f'The factorial of {n} is: ', factorial(n))
