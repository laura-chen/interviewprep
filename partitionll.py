# Partition: Write code to partition a linked list around a value x, such that
# all nodes less than x come before all nodes greater than or equal to x. lf x
# is contained within the list, the values of x only need to be after the
# elements less than x (see below).The partition element x can appear anywhere
# in the "right partition"; it does not need to appear between the left and
# right partitions.
#
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5)
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Node(self, data):
    def __init__:
        self.data = 0
        self.next = None

def partition(node, pivot):
    head, tail = node, node
    while node:
        next = node.next
        if node.data < pivot:
            node.next = head
            head = node
        else:
            node.next = tail
            tail = node
        node = next
    tail.next = None
    return head
