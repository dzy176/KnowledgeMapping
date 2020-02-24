def find_permutation(s, pattern):
    patternDict = {}
    for ch in pattern:
        if ch in patternDict:
            patternDict[ch] += 1
        else:
            patternDict[ch] = 1

    sDict = {}

    windowStart = 0

    for windowEnd in range(len(s)):
        if s[windowEnd] in sDict:
            sDict[s[windowEnd]] += 1
        else:
            sDict[s[windowEnd]] = 1
        if windowEnd - windowStart + 1 > len(pattern):
            sDict[s[windowStart]] -= 1
            if sDict[s[windowStart]] == 0:
                del sDict[s[windowStart]]
            windowStart += 1
        print sDict, patternDict
        if sDict == patternDict:
            return True
    return False

print find_permutation("oidbcaf", "abc")