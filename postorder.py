# Given the root for a binary tree, perform a post-order traversal and return
# the resulting list of values.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorderTraversal(root):
    nodes = []
    if root:
        recurseTree(nodes, root)
    return nodes

def recurseTree(nodes, root):
        if root.left:
            recurseTree(nodes, root.left)
        if root.right:
            recurseTree(nodes, root.right)
        nodes.append(root.val)
