"""
File: linked_list.py
"""


def insert(n0, P):
    """ 在链表的结点 n0 之后插入结点 P """
    n1 = n0.next
    P.next = n1
    n0.next = P


def remove(n0) -> None:
    """ 删除链表的结点 n0 之后的首个结点 """
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1


def find(head, target):
    """ 在链表中查找值为 target 的首个结点 """
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1


