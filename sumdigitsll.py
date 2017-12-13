'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes
contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

def add_numsll(l1, l2):
  fake_head = Node(0)
  curr_new = fake_head
  carry = 0
  while l1 or l2 or carry:
    l1_val = l1.val if l1 else 0
    l2_val = l2.val if l2 else 0

    new_val = (l1_val + l2_val + carry) %10
    carry = (l1_val + l2_val + carry)/10
    curr_new.next = Node(new_val)
    curr_new = curr_new.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
  return fake_head.next


Class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
