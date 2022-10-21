'''uilt in funtion len()
input = one list
output = whole number that represents the length of that list
List can tale different formats
'''
# Consideting string, len on string considere the number of characters
firsName = "Taylor"
print(len(firsName))

lastname = "Swift"
print(len(lastname))

print(firsName.__len__())

# Consideting integers in a list
ages = [0, 11, 43, 12, 10]
print(len(ages))
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(["bob", "marry", "san"]))

candy_colletion = {"bob" :10, "marry" :7, "sam" :18}
print(len(candy_colletion))