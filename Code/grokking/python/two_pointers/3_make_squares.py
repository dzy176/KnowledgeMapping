# coding=utf-8

# 左右指针往中间走，谁的平方值比较大就放入数组，并向中间移动

def make_squares(arr):
    arr_len = len(arr)
    res = [0 for x in range(arr_len)]

    left, right = 0, arr_len - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square < right_square:
            res[arr_len - 1] = right_square
            right -= 1
        else:
            res[arr_len - 1] = left_square
            left += 1
        arr_len -= 1
    return res


print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
