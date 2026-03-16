class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Step 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# Example usage
s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))  
# Output: [[1,5],[6,9]]

print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
# Output: [[1,2],[3,10],[12,16]]

print(s.insert([[4,7],[8,10]], [1,3]))  
# Output: [[1,3],[4,7],[8,10]]
