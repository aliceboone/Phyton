#   array class
# expenses = [['jan', 2200], ['feb', 3250], ['mar', 2600], ['apr', 2130], ['may', 2190]]
#
# for element in expenses:
#     if element == "feb":
#         print(element[1])

# for element in expenses:
#     diff = expenses[2] - expenses[1]
# print(diff)
#
# first_qtr_expenses = expenses[0] + expenses[1] + expenses[2]
# print(first_qtr_expenses)
#
# average = sum(expenses)/len(expenses)
# print(average)
#
# expenses.append(1980)
#
# expenses[3] = 1930
#
# print(expenses)
#
# # hash class
#
expenses = {'jan', 2200, 'feb', 3250, 'mar', 2600, 'apr', 2130, 'may', 2190}

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

print(get_hash("d"))

