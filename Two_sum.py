'''Give an array of integers, return indices of the two numbers such that they add up to a specific target
You may assume that each input would have exactly one solution, and you may not use the same element twice

Input = [2, 7,
Output =
'''

def twoSum(array, target):
    hash = {}

    for i, n in enumerate(array):
        diff = target - n
        if diff in hash:
            return[hash[diff], i]
        hash[n] = i
    return
print(twoSum([2, 7, 4, 1], 3))



