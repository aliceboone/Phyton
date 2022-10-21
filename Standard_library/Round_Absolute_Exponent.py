''' ROUND
Input = one whole or decimal number
Output = integer that represents the inputed number, rounded up or down depending on its value
if decimal digit 4 or bellow - round down
if decimal digit 5 or above - round up
'''


myGPA = 3.6
print(round(myGPA))

amountOfSalt = 1.4
print(round(amountOfSalt))

apple = 1.2
print(round(apple))

google = -1.6
print(round(google))

'''ABS 
abs stands fro absolut value
input - one whole or decimal number
output - number representing the absolute value of the inputed number
if positive number -> same number will be returned
if negative number -> positive version of inputed returned
'''
distanceAway = -13
print(abs(distanceAway))

lengthOfRootInGround = 2.5
print(abs(lengthOfRootInGround)) # does not round

''' POW
input - two whole or decimal numbers
    first input - base
    second input - exponent
output - number representing the result of the exponentiation
    3^2 pow(3,2) = 9
'''

chanceOfTails = 0.5
inARowTails = 3
print(pow(chanceOfTails, inARowTails))

chanceOfOne = .167
inARowOne = 2
print(pow(chanceOfOne, inARowOne))