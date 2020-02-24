def find_permutation(str, pattern):
    patternDict = {}
    for x in pattern:
        if x in patternDict:
            patternDict[x] += 1
        else:
            patternDict[x] = 1

    minLen = len(str) + 1
    windowStart = 0
    matched = 0
    res = ""

    for windowEnd in range(len(str)):
        endChar = str[windowEnd]
        if endChar in patternDict:
            patternDict[endChar] -= 1
            if patternDict[endChar] >= 0:
                matched += 1

    while matched == len(pattern):

        if minLen < windowEnd-windowStart+1:
            res = str[windowStart:windowEnd+1]

        startChar = str[windowStart]
        windowStart += 1
        if startChar in patternDict:
            patternDict[startChar] += 1
            if patternDict[startChar] == 0:
                matched -= 1

    return res



