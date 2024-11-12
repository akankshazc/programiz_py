# Python program to find HCF (highest common factor) or GCD (greatest common divisor) of two numbers

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))


# Using the euclidean algorithm
def hcf_euclidean(x, y):
    while y:
        x, y = y, x % y
    return x


print("The HCF of", num1, "and", num2, "is", hcf_euclidean(num1, num2))
