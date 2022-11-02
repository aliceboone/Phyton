'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]

Constraints
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

def topFrequent(nums, k):

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        count[i] = 1 + count.get(i, 0)

    for i, c in count.items():
        freq[c].append(i)
    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topFrequent([1, 1, 1, 2, 2, 3], 2))
print(topFrequent([1, 1, 1, 1, 1, 1], 1))