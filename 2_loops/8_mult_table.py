# Multiplication table (from 1 to 10)

num = int(input("Enter a number: "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
