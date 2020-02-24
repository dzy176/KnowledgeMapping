# coding=utf-8

from collections import deque


def find_subarrays(arr, target):
    res = []
    product = 1
    window_start = 0
    for window_end in range(len(arr)):
        product *= arr[window_end]

        # 确保window中数据符合要求
        while product >= target and window_start < window_end:
            product /= arr[window_start]
            window_start += 1

        # 对窗口数据进行操作
        temp_list = deque()
        for i in range(window_end, window_start - 1, -1):
            temp_list.appendleft(arr[i])
            res.append(list(temp_list))
    return res


print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))
