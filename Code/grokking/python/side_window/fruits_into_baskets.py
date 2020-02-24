def fruits_into_baskets(fruits):
    windowStart, maxFruits = 0, 0
    fruitsDict = {}

    for windowEnd in range(len(fruits)):
        if fruits[windowEnd] not in fruitsDict:
            fruitsDict[fruits[windowEnd]] = 1
        else:
            fruitsDict[fruits[windowEnd]] += 1

        while len(fruitsDict) > 2:
            fruitsDict[fruits[windowStart]] -= 1
            if fruitsDict[fruits[windowStart]] == 0:
                del fruitsDict[fruits[windowStart]]
            windowStart += 1
        maxFruits = max(maxFruits, windowEnd - windowStart + 1)
    return maxFruits


print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
