# coding=utf-8

# https://changsiyuan.github.io/2016/07/20/2016-7-20-roll-linkedlist/

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# 快慢指针第一次相遇时，慢指针走过的长度就是环长（证明过程见上连接）
def find_cycle_length(head):
    slow, fast = head, head
    fast_len, slow_len = 0, 0
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        slow_len += 1
        if slow == fast:
            return slow_len
    return 0