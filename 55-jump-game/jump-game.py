class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                # If current index is beyond the furthest reachable, fail
                return False
            maxReach = max(maxReach, i + nums[i])
        return True


# Example usage
s = Solution()
print(s.canJump([2,3,1,1,4]))  # Output: True
print(s.canJump([3,2,1,0,4]))  # Output: False

