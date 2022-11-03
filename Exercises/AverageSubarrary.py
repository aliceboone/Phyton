'''Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
Input [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output = [2.2, 2.8, 2.4, 3.6, 2.8]
'''

def find_ave_subarrays(array, k):
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

print(find_ave_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
