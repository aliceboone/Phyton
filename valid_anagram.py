'''Given two strings s and t, return true if t is an anagram of s, and false otherwise
anagram is when 2 diferente words are made up using the exact same amount of characters

Input = s = 'anagram', t = 'nagaram'
Output = true

Input = s = 'rat', t = 'car'
Output = false

time complexity = O(n)
space complexity = O(n)
'''


def isAnagram(s, t):

    if len(s) != len(t):
        return False
    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

print(isAnagram("poc", "cop"))
print(isAnagram("car", "tap"))
print(isAnagram("true", "tru"))
