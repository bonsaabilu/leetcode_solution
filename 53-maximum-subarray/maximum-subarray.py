class Solution(object):
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross_sum = self.crossSum(nums, left, right, mid)
        
        return max(left_sum, right_sum, cross_sum)

    def crossSum(self, nums, left, right, mid):
        # Max sum crossing the midpoint
        left_max = float('-inf')
        curr = 0
        for i in range(mid, left - 1, -1):
            curr += nums[i]
            left_max = max(left_max, curr)
        
        right_max = float('-inf')
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            right_max = max(right_max, curr)
        
        return left_max + right_max

