# Python Program to compute the power of a number

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))


# Using a for loop
def power(base, exponent):
    result = 1
    if exponent >= 0:
        for _ in range(exponent):
            result *= base
    # for negative exponents
    else:
        for _ in range(-exponent):
            result /= base
    return result


# Using the pow()
result = pow(base, exponent)

print(f"{base} raised to the power of {exponent} is {result}")

print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
