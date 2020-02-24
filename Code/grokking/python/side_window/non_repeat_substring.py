def non_repeat_substring(str):
    windowStart, maxSize = 0, 0
    charDict = {}

    for windowEnd in range(len(str)):
        if str[windowEnd] not in charDict:
            charDict[str[windowEnd]] = windowEnd
            maxSize = max(maxSize, windowEnd - windowStart + 1)
        else:
            windowStart = max(windowStart, charDict[str[windowEnd]] + 1)
    return maxSize


print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
