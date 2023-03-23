'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,2,3,4]
# Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true'''


#
# def containsDuplicates(nums):
#     if not nums or len(nums) == 0:
#         return False
#
#     hashset = set()
#
#     for n in nums:
#         if n in hashset:
#             return True
#         hashset.add(n)
#     return False
#
# print(containsDuplicates([]))
# print(containsDuplicates([1,2,3,1]))
# print(containsDuplicates([1,2,3,4]))
# print(containsDuplicates([1,1,1,3,3,4,3,2,4,2]))
# class Player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def damage(self, pts):
#         self.health -= pts
#
#     a = Player(2, 3)
#     a.damage(2)
#     a.move(1, 2)
#     print(a.x + a.y + a.health)

height = 100
bounce = 1
while bounce <= 3:
    height = height * (3/5)
    bounce += 1
newheight = height;
print(newheight)
