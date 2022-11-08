'''Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".'''

def longestSubstring(strs, k):
    # create variables
    hash = {}
    start = 0
    max_length = 0

    # loop over string
    for i in range(len(strs)):
        #  build the hash map
        if strs[i] not in hash:
            hash[strs[i]] = 1
        else:
            hash[strs[i]] += 1

    while len(hash) > k:
        hash[strs[start]] -= 1

    max_length = max(max_length, i + 1)

    return max_length

print(longestSubstring("araaci", 2))
print(longestSubstring("araaci", 1))
print(longestSubstring("cbbebi", 3))
print(longestSubstring("cbbebi", 10))

