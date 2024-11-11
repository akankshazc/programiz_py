# Python program to check if the number is an Armstrong number or not

num = input("Enter a number: ")

# initialize sum
sum = 0

# find the sum of the number raised to power n of each digit
for i in num:
    sum += int(i) ** len(num)

# display the result
if sum == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
