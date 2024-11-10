# Python program to convert temperature in celsius to fahrenheit

# celcius input
celsius = float(input('Enter temperature in Celsius: '))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32

print('%0.1f degree Celcius is equal to %0.1f degree Fahrenheit' %
      (celsius, fahrenheit))
