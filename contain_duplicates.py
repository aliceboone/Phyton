'''
Given an array of numbers, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums=[1, 2, 3, 1]
Output: true

Input: nums=[1, 2, 3, 4]
Output: false

Input: nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true

Time complexity = O(n)
Space complexity = O(n)
'''


def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
