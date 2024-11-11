# return the fibonacci sequence less than n

def fibonacci_less_than(n):
    seq = [0, 1]
    num1 = 1
    num2 = 1
    while num2 < n:
        seq.append(num2)
        num2 = num2 + num1
        num1 = seq[-1]

    return seq


# Test the function
n = int(input("Enter a number: "))

print(fibonacci_less_than(n))
