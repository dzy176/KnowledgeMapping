# coding=utf-8

# X+Y+Z = 0, 即 -X = Y+Z
# 找出X元素后面的所有元素中，之和为-X的，就符合要求，注意去重s

def search_triplets(arr):
    arr.sort()
    triplets = []

    for left in range(len(arr)):
        if left > 0 and arr[left] == arr[left - 1]:
            continue
        search_pair(arr, -arr[left], left+1, triplets)
    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif arr[left] + arr[right] < target_sum:
            left += 1
        else:
            right -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))
