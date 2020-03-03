# coding=utf-8

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse(head):
    pre = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def reorder(head):
    half = find_middle_of_linked_list(head)
    first = head
    half_reversed = reverse(half)

    while first is not None and half_reversed is not None:
        # 反转过的后半截，每次把头部pop掉
        # 前半部分，两两节点插入之
        poped = half_reversed
        half_reversed = half_reversed.next

        next = first.next
        first.next = poped
        poped.next = next
        first = next
    if first is not None:
        first.next = None

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    while head is not None:
        print head.value
        head = head.next
