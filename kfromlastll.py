# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
# Ex. 1 -> 4 -> 5 -> 6 -> 7 -> 1. Get 2nd from last: 7
#                    |         |
# Runner method

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def kFromLast(node, k):
    faster, slower = node, node

    for i in range(k):
        if not faster:
            return None
        faster = faster.next

    while faster:
        faster, slower = faster.next, slower.next

    return slower
