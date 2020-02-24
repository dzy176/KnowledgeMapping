# coding=utf-8

def longest_substring_with_k_distinct(str, k):
    windowStart, maxSize = 0, 0
    charDict = {}

    for windowEnd in range(len(str)):
        if str[windowEnd] not in charDict:
            charDict[str[windowEnd]] = 1
        else:
            charDict[str[windowEnd]] += 1

        while len(charDict) > k:
            charDict[str[windowStart]] -= 1
            if charDict[str[windowStart]] == 0:
                del charDict[str[windowStart]]
            windowStart += 1
        maxSize = max(maxSize, windowEnd - windowStart + 1)
    return maxSize


print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
