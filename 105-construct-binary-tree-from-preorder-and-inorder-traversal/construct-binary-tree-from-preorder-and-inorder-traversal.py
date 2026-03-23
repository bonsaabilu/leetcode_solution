class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            in_root_index = inorder_index[root_val]
            left_size = in_root_index - in_left
            
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root_index - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, in_root_index + 1, in_right)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
