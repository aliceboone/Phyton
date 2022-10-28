'''Math'''

import math

#Constants
print(math.pi)
print(math.e)
print(math.nan)
print(math.inf)
print(-math.inf)

#Trigonometry
'''
Just to review cosine measures the adjacent side over the hypotenuse and sine measures the opposite side over the hypotenuse. This means the X portion here is like the cosine value, and the Y portion is like the sine value. At a 45 degree angle, these are mathematically the same. In the code, we can also prove that they have the same value
'''
obst_direction = math.cos(math.pi/4)
print(obst_direction)
obst_direction = math.sin(math.pi/4)
print(obst_direction)


#Ceiling and Floor
cookies = 10.3
candy = 7

print(math.ceil(cookies))
print(math.ceil(candy))

age = 47.9
other_age = 47
print(math.floor(age))
print(math.floor(other_age))



