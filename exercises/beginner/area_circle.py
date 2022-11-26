# Exercise Request to the user the radio of the circle to calculate the area

import math

def area_circle(radio):
    PI = math.pi
    return PI * (radio ** 2)

circle_input = float(input('Please enter the radio: '))

result = round(area_circle(circle_input),2)

print(f'According to the radio, the result is {result}')

