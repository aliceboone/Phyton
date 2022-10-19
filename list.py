nums = [25, 12, 36, 95, 14]
print(nums[1])
print(nums[4])
print(nums[2:]) # get nums starting at index 2

name = ["Navin", "Anna", "John"]

'''
price_1 = 20
price_2 = 50
proce_3 = 200
'''
#         0   1   2 - List has index that starts at 0
price = [20, 50, 200]
print(price[1])
print(price.index(200)) # here we can prince the index related to the price 200 which is 2

for item in price:
    print(item)

diversities = [15, "John", True]
print(diversities[0])
print(diversities[1])
print(diversities[2])

for diversitie in diversities:
    print(diversitie)

'''Sum of values - give a list of ages, sum the values
1 - list of ages
2 - create a variable to hold the total
3 - loop over the ages
4 - sum the total + ages
5 - print total
'''
ages = [15, 46, 75, 34, 23]
total = 0

for age in ages:
    total = total + age
print(total)


