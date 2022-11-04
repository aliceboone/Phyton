'''Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].'''

import math
def smallest_subarray_sum(array, s):

    min_length = math.inf
    sum = 0
    start_point = 0

    for i in range(0, len(array)):
        sum = sum + array[i] # Add the next element
        while sum >= s:
            min_length = min(min_length, i - start_point + 1)
            sum = sum - array[start_point]
            start_point += 1

    if min_length == math.inf:
        return 0
    return min_length

print(smallest_subarray_sum([1, 2, 1, 2  ], 7))
print(smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_sum([2, 1, 5, 2, 8], 7))
print(smallest_subarray_sum([3, 4, 1, 1, 6], 7))