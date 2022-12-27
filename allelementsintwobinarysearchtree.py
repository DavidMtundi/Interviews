"""
Given two trees return the sorted merged list
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1, root2):
        res = []

        def inorder(root):
            if root is None:
                return 0
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root1)
        inorder(root2)

        return sorted(res)
