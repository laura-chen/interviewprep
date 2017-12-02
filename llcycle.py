# Given the head of a singly-linked list, determine whether or not the list has
# a cycle.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    slow = fast = head
    while slow and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False
