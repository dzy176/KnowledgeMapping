# coding=utf-8

# 给定list，求连续k个数的平均数

def find_averages_of_subarrays(k, arr):
    res = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd - windowStart == k-1:
            res.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return res

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print result

main()

