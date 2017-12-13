# Given a singly linked list where each node also contains a pointer to a random
# other node in the list, copy the list to a new list that preserves all of the
# same relationships between nodes
#
# Example:
# Input
# 	------		------		------
# 	-	 -		-	 -      -    -
# 	- 1  -  -->	- 2  - ---> - 3  ---> null
# 	-	 -		-    -      -    -
# 	------		------      ------
# 	  |         |_^  ^       ^ |
# 	  |              |       | |
# 	  |----------------------  |
# 	                 |         |
# 	                 -----------
# Output:
#
# Input
# 	------		------		------
# 	-	 -		-	 -      -    -
# 	- A  -  -->	- B  - ---> - C  ---> null
# 	-	 -		-    -      -    -
# 	------		------      ------
# 	  |         |_^  ^       ^ |
# 	  |              |       | |
# 	  |----------------------  |
# 	                 |         |
# 	                 -----------

Class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    
def copy_rels(head):
    curr_idx, current = 0, head
    pointer_dict = {}
    current2 = Node(current.val) #Create copy of the head
    head2 = current2
    while current:
        pointer_dict[current] = curr_idx
        current2.next = Node(current.next.val)
        curr_idx += 1
        current = current.next
    current = head
    current2 = head2
    while current:
        distance = pointer_dict[current.rand] #index of current.rand
        rand = copy_head # pointer to find the corresponding .rand node in copied list.
        for i in range(distance):
            rand = rand.next
            current2.rand = rand
        current = current.next
        current2 = current2.next
    return head2
