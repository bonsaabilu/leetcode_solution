class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        
        from functools import lru_cache
        
        @lru_cache(None)
        def build(start, end):
            if start > end:
                return [None]
            
            res = []
            
            for root_val in range(start, end + 1):
                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)  # Use LeetCode's TreeNode
                        root.left = left
                        root.right = right
                        res.append(root)
            
            return res
        
        return build(1, n)