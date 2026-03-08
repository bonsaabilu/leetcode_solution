from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        res = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1  # Two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Need a bigger number
                else:
                    right -= 1  # Need a smaller number
        
        return res