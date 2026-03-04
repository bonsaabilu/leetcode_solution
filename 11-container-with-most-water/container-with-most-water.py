class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Two pointers: left starts at beginning, right at the end
        left = 0
        right = len(height) - 1
        
        max_water = 0
        
        # Keep moving until pointers meet
        while left < right:
            # Area = width × min(height of two lines)
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            
            # Update max if current is bigger
            if current_area > max_water:
                max_water = current_area
            
            # Move the pointer with smaller height
            # (because we want to try to find taller height to increase area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water