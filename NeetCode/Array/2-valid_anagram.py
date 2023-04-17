'''Given two strings s and t, return true if t is an anagram of s, and false otherwise
anagram is when 2 diferente words are made up using the exact same amount of characters

Input = s = 'anagram', t = 'nagaram'
Output = true

Input = s = 'rat', t = 'car'
Output = false

time complexity = O(n)
space complexity = O(n)
'''


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        # build a hash for s and t
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # iterate over s and check if s and an t are diff, if its different return False
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)
#

solution = Solution()
print(solution.isAnagram("true", "tru"))
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("car", "rat"))
