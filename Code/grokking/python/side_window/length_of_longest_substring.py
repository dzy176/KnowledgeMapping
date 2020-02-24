# coding=utf-8

# 1. 右窗口不断扩大，每次计算出当前窗口中最大的重复字符串的个数
# 2. 整个窗口中剩余的字符正好是k个，高于k个则表明当前窗口不符合预期，左窗口右移
# 3. 整个过程，保证了当前框住的窗口大小的字符串是符合要求的

def length_of_longest_substring(str, k):
    windowStart, maxLen, maxRepeat = 0, 0, 0
    charDict = {}
    for windowEnd in range(len(str)):
        endChar = str[windowEnd]
        if endChar in charDict:
            charDict[endChar] += 1
        else:
            charDict[endChar] = 1

        maxRepeat = max(maxRepeat, charDict[endChar])

        if windowEnd - windowStart + 1 - maxRepeat > k:
            startChar = str[windowStart]
            charDict[startChar] -= 1
            windowStart += 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen


print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))
