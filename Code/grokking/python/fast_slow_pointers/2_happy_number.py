# coding=utf-8

# 如果平方和最终陷入一个循环，这个循环只会存在两种情况：
# 一种是循环有且只有一个1（快乐数）
# 一种是必然没有1（非快乐数）
# 所以相遇的时候只要不是1，必然是不是快乐数
def suq_sum(num):
    tmp_sum = 0
    while num > 0:
        tmp = num % 10
        tmp_sum += tmp * tmp
        num = num / 10
    return tmp_sum

def find_happy_num(num):
    slow, fast = num, num
    while True:
        slow = suq_sum(slow)
        fast = suq_sum(suq_sum(fast))
        if slow == fast:
            break
    return slow == 1