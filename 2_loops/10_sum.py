# Function to calculate the sum of all digits in a given number

def sum_of_digits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum


# Test the function
n = int(input("Enter a number: "))

print(f'sum of all digits in number {n} is:', sum_of_digits(str(n)))
