# factorial with for loop
def factorial(n):
    factorial = 1
    for x in range(1, n+1):
        factorial = factorial * x
    return factorial
