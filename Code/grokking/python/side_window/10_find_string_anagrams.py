# coding=utf-8

# 找出所有符合pattern字符串的下标


def find_string_anagrams(str, pattern):
    res = []
    windowStart = 0
    patternDict, strDict = {}, {}
    for x in pattern:
        if x in patternDict:
            patternDict[x] += 1
        else:
            patternDict[x] = 1

    for windowEnd in range(len(str)):
        if str[windowEnd] in strDict:
            strDict[str[windowEnd]] += 1
        else:
            strDict[str[windowEnd]] = 1

        if windowEnd - windowStart + 1 > len(pattern):
            strDict[str[windowStart]] -= 1
            windowStart += 1
            if strDict[str[windowStart]] == 0:
                del strDict[str[windowStart]]

        if strDict == patternDict:
            res.append(windowStart)
    return res


print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))
