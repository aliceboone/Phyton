'''Sorted
Input - one iterable(somethong we can iterate through)
- lists, tuples, strings, dictionaries, et
Output = List with the items from the input sorted
Optional parameters - reverse or not? case sensitive or not?
'''

# least to gratest
pointInaGame = [0, -10, 15, -2, 1, 12]
print(sorted(pointInaGame))

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointInaGame, reverse=True))

leaderBoard = {231 :"CKL", 123 :"ABC", 432 :"JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard[432])
print(leaderBoard.get(432))


students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))