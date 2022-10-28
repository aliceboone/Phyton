'''
Input = one whole number
output = range instance that holds all the numbers counting by one between 0 and the input
Optional, parameters = starting pint - count(by 1, 2, ,3 4)
'''

numberContestants = range(30)

print(list(numberContestants))

for c in numberContestants:
    print("Contestant " + str(c) + " is here")

luck_winners = range(7, 30, 5) # list de numbers de 7 a 30 counting de 5 em 5
print(list(luck_winners))  #[7, 12, 17, 22, 27]