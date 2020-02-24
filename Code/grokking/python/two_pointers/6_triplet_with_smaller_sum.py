def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for left in range(len(arr) - 2):
        middle = left + 1
        right = len(arr)-1

        while middle < right:
            if arr[left] + arr[middle] + arr[right] >= target:
                right -= 1
            else:
                count += right-middle
                middle += 1

    return count


print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
