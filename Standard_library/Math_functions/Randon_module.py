import random

# Randon Numbers
print(random.random())
decider = random.randrange(2)
if decider == 0:
    print("heads")
else:
    print("tails")
print(decider)

print("you rolled a " + str(random.randrange(1, 7)))

# Randon Choices

lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

cards = ["Jack", "King", "Queen", "Ace"]
print(random.choice(cards))