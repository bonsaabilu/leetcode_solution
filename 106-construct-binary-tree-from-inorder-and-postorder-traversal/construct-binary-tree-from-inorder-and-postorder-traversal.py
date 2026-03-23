# LeetCode already provides the TreeNode class, so don't redefine it.

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = postorder.pop()   # last element in postorder is the root
            root = TreeNode(root_val)
            
            in_root_index = inorder_index[root_val]
            
            # build right subtree first (because of postorder popping from the end)
            root.right = helper(in_root_index + 1, in_right)
            root.left = helper(in_left, in_root_index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
