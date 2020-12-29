"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def helper(node):
            if not node:
                return False
            mid = node == p or node == q
            left = helper(node.left)
            right = helper(node.right)
            if (left + right + mid) >= 2:
                print(node.val)
                self.lca = node
            return left or right or mid
        helper(root)
        return self.lca
            