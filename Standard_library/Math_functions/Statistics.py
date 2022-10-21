'''Review statistics
Given [2, 2, 3]
Mean(average) = 7/3 = 2.3333333
median(midpoint) = 2
Mode(most frequent value) = 2
'''
import math
import statistics

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]
print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

'''Review advanced statistics
Given [2, 2, 3]
Variance - The average of the squared differences from the mean
[(2 - 2.33) + (2 - 2.33) + (3 - 2.33)2 / (3 - 1) = 1/3
Standard deviation: the square root of the variance
    square root of 1/3 = 0.5735
'''

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))