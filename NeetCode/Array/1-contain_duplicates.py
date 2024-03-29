'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,2,3,4]
# Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
'''


class Solution(object):
    def containsDuplicates(self, nums) -> bool:
        if not nums or len(nums) == 0:
            return False

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



solution = Solution()
print(solution.containsDuplicates([]))
print(solution.containsDuplicates([1, 2, 3, 1]))
print(solution.containsDuplicates([1, 2, 3, 4]))
print(solution.containsDuplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
