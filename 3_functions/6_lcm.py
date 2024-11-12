# Python program to find LCM (least common multiple) of two numbers

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))

# Using the euclidean algorithm


def hcf_euclidean(x, y):
    while y:
        x, y = y, x % y
    return x

# Using the formula LCM(x, y) = x * y / HCF(x, y)


def lcm_formula(x, y):
    return x * y // hcf_euclidean(x, y)


print("The LCM of", num1, "and", num2, "is", lcm_formula(num1, num2))
