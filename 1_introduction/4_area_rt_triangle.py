# function to calculate area of right angled triangle rounded off to two decimal places

def triangle_area(base, height):
    area = (base ** 2 + height ** 2) ** 0.5
    return area


base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

print(triangle_area(base, height))
