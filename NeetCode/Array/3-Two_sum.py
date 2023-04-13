'''Give an array of integers, return indices of the two numbers such that they add up to a specific target
You may assume that each input would have exactly one solution, and you may not use the same element twice

Input = [2, 7, 11, 15], target = 9
Output = [0, 1]


'''

def twoSum(nums, target):
    if not nums or len(nums) == 0:
        return "nums is empty"

    hash_num = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash_num:
            return [hash_num[diff], i]
        hash_num[n] = i

print(twoSum([], 0))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 1, 5], 7))

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         if (target - nums[i]) in nums[i + 1:]:
#             return True
#     return False
#
# print(two_sum([], 0))
# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([2, 3, 1, 5], 7))


