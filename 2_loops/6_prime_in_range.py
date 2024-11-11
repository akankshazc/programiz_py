# Function to check if a number is prime within a given range

def is_prime_in_range(n, start, end):
    if n > 1:
        for i in range(start, end):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


# Test the function
n = int(input("Enter a number: "))
start = int(input("Enter lower range: "))
end = int(input("Enter upper range: "))

print(is_prime_in_range(n, start, end))
