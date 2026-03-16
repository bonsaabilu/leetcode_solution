class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()  # sort to handle duplicates
        used = [False] * len(nums)
        self.backtrack(nums, [], used, results)
        return results

    def backtrack(self, nums, path, used, results):
        if len(path) == len(nums):
            results.append(list(path))  # store a valid permutation
            return
        for i in range(len(nums)):
            # Skip already used elements
            if used[i]:
                continue
            # Skip duplicates: only use the first occurrence unless the previous duplicate was used
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, path, used, results)
            path.pop()
            used[i] = False
