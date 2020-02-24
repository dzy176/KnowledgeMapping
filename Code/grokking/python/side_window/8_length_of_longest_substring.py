def length_of_longest_substring(arr, k):
    windowStart, maxLen, maxRepeatOne = 0, 0, 0
    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 1:
            maxRepeatOne += 1
        if windowEnd - windowStart + 1 - maxRepeatOne > k:
            if arr[windowStart] == 1:
                maxRepeatOne -= 1
            windowStart += 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen


print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
