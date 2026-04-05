class Solution:
    def minOperations(self, nums):
        stack = []
        operations = 0
        
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            
            if num > 0 and (not stack or stack[-1] < num):
                operations += 1
                stack.append(num)
        
        return operations