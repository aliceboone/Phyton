'''Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sum_subarray(array, k):

    max_sum = 0
    start_point = 0
    sum = 0

    for i in range(len(array)):
        sum = sum + array[i] # add the next element
        if i >= k - 1:
            max_sum = max(max_sum, sum)
            sum -= array[start_point]
            start_point += 1
    return max_sum

    result = []
    start_point = 0
    sum = 0

    for i in range(len(array)):
        sum = sum + array[i]
        if i >= k - 1:
            result.append(sum / 5)
            sum = sum - array[start_point]
            start_point += 1

    return result




print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print(max_sum_subarray([2, 3, 4, 1, 5], 2))