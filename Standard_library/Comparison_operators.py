# Python Comaprison Operators
#  TIPS
#  == --> is equal to
kitten = 10
tiger = 75

if kitten < tiger:
    print("the kitten weighs less than the tiger")

#  <= --> is less than or equal to
mouse = 1
if mouse < kitten and mouse < tiger:
    print("the mouse weights less ")

# A - Z --> 1 - 26
print("a" <= "b") # a will be mapped to 1 and b will be mapped to 2

#  >= --> is greater than or equal to
# False --> 0
# True --> 1
print(False > True)  # return False because True is greater

# > --> is greater than
# Looking for first mismatched letter
# A - Z --> 1 - 26

print("Jennifer" > "Jenny")  # False is comparing i and y since from 1-26 i = 9 and y = 25 Jenny is greater

#  < --> is less than
print(10  < 75)
print(75 < 10)
if 10 < 75:
    print("the bigger number is bigger")


