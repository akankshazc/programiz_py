# Python function to find the smallest among three numbers

def find_smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print(f'the smallest number among {a}, {
      b} and {c} is:', find_smallest(a, b, c))
