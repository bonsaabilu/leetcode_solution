# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Case 1: both are None → trees match here
        if not p and not q:
            return True
        
        # Case 2: one is None, the other is not → mismatch
        if not p or not q:
            return False
        
        # Case 3: values differ → mismatch
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
