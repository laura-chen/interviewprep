# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#      The left subtree of a node contains only nodes with keys less than the node's
#      key.
#      The right subtree of a node contains only nodes with keys greater than the
#      node's key.
#      Both the left and right subtrees must also be binary search trees.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recurseBST(root, float('-inf'), float('inf'))

    def recurseBST(self, root, min, max):
        if not root:
            return True
        if not min < root.val or not root.val < max:
            return False
        if not self.recurseBSTk(root.left, min, root.val) or not self.recurseBST(root.right, root.val, max):
            return False
        return True
