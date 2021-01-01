"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def compare(root, comp):
            if comp == None and root == None:
                return True
            if comp == None or root == None or root.val != comp.val:
                return False
            return compare(root.left, comp.left) and compare(root.right, comp.right)
        return s and (compare(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))