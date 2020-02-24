# coding=utf-8
# 给定数组，求连续k个数之和的最大值
def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]
        if windowEnd >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[windowStart]
            windowStart += 1
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
