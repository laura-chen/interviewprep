# Given the head nodes of two lists, determine whether the two lists intersect
# at a node. Return the intersecting node if they intersect and False otherwise.

# If two lists have the same last node, we know they must intersect. Uses result
# from find_length_last to determine whether lists intersect. Calls
# advance_pointer, then finds intersecting node.
def find_intersection(l1, l2):
    lengthlast1 = find_length_last(l1)
    lengthlast2 = find_length_last(l2)
    if lengthlast1[1] != lengthlast2[1]:
        return False
    s1, s2 = l1, l2
    if lengthlast1[0] > lengthlast2[0]:
        advance_pointer(s1, lengthlast1[0], lengthlast2[0])
    if lengthlast2[0] > lengthlast1[0]:
        advance_pointer(s2, lengthlast2[0], lengthlast1[0])
    while s1 != s2:
        s1 = s1.next
        s2 = s2.nexts
    return s1

# Helper function to advance the start pointer for the longer list to be the same
# distance from the last node as the start pointer for the shorter list.
def advance_pointer(start, long_length, short_length):
    for i in range (0, long_length-short_length):
        start = start.next

# Helper function that takes a head node as input and returns a tuple containing
# the length of the list and a pointer to the last node.
def find_length_last(node):
    current = node
    length = 0
    last = none
    while current.next:
        length += 1
        current = current.next
    last = current
    return (length, last)
