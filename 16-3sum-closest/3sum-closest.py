from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        # Initialize the closest sum with a large value
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Step 2: Iterate through the array
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If this sum is closer to target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Need a bigger sum
                elif current_sum > target:
                    right -= 1  # Need a smaller sum
                else:
                    # Exact match found
                    return current_sum
        
        return closest_sum
        