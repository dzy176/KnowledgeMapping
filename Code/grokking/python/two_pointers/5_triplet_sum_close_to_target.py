# coding=utf-8

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()

    smallest_diff = target_sum - arr[0] - arr[1] - arr[2]

    for left in range(len(arr) - 2):
        middle = left + 1
        right = len(arr)-1

        while middle < right:
            current_sum = arr[left] + arr[middle] + arr[right]

            current_diff = target_sum - current_sum

            if current_diff == 0:
                return target_sum

            if abs(current_diff) < abs(smallest_diff) or abs(current_diff) == abs(
                    smallest_diff) and current_diff > smallest_diff:
                smallest_diff = current_diff

            if current_diff > 0:
                middle += 1
            else:
                right -= 1

    return target_sum - smallest_diff


print(triplet_sum_close_to_target([1, 2, 3, 4], 2))
print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
