'''Whats is a Boolean'''
isRaining = True
isSunny = False

'''Local Operators - takes one or more boolean values and operate on then
AND
true and true -> true
false and true -> true
true and false -> true
false and false -> false
'''

if isRaining and isSunny:
    print("We might see a rainbow")

'''OR
true and true -> true
false and true -> true
true and false -> true
false and falase -> false'''

if isRaining or isSunny:
    print("It might be raining or might be sunny")

''''NOT
true -> not
not -> false'''

if not isRaining:
    print("It must be raining")

ages = [12, 18, 39, 87, 7, 2]

for age in ages:
   isAdult = age > 17
   if not isAdult:
       print("Being " +str(age) + " does not make you an adult.")




