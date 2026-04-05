import math

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        
        # Step 1: count ones
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # Step 2: find shortest subarray with gcd = 1
        min_len = float('inf')
        
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        # Step 3: check if possible
        if min_len == float('inf'):
            return -1
        
        return min_len + n - 2