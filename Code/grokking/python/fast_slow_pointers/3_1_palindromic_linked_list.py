# coding=utf-8

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    pre = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def is_palindromic_linked_list(head):
    if head is None or head.next is Node:
        return True
    middle = find_middle_of_linked_list(head)
    middleReverserd = reverse(middle)
    middleReverserdCopy = middleReverserd
    while middleReverserdCopy is not None:
        if head.value != middleReverserdCopy.value:
            break
        middleReverserdCopy = middleReverserdCopy.next
        head = head.next

    # recover
    reverse(middleReverserd)
    # 这点不容易考虑到，原回文的长度为技术、偶数，判读条件可能不一致
    if middleReverserd is None or head is None:
        return True
    return False

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))