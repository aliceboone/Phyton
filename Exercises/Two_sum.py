'''Give an array of integers, return indices of the two numbers such that they add up to a specific target
You may assume that each input would have exactly one solution, and you may not use the same element twice

Input = [2, 7, 11, 15], target = 9
Output = [0, 1]


'''

def twoSum(nums, target):
    if not nums or len(nums) == 0:
        return "nums is empty"

    preMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in preMap:
            return [preMap[diff], i]
        preMap[n] = i

print(twoSum([], 0))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 1, 5], 7))


