# factorial with for loop
def factorial(n):
    factorial = 1
    if n < 0:
        print('Sorry, factorial does not exist for negative numbers')
    elif n == 0:
        print('The factorial of 0 is 1')
    else:
        for x in range(1, n+1):
            factorial = factorial * x
        return factorial


# Testing the function
n = int(input("Enter a number: "))

print(f'The factorial of {n} is: ', factorial(n))
