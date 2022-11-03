'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

def isPalindrome(s):

    res = ""
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not alphaNum(s[i]):
            i += 1
        while j > i and not alphaNum(s[j]):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i +=1
        j -= 1
    return True

    # for c in s:
    #     if c.isalnum():
    #         res += c.lower()
    # return res == res[::-1]

def alphaNum(c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(""))
