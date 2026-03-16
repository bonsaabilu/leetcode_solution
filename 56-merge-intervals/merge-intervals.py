class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        # Step 2: Iterate and merge
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]
            
            if curr[0] <= prev[1]:
                # Overlap → merge
                merged[-1][1] = max(prev[1], curr[1])
            else:
                # No overlap → add new interval
                merged.append(curr)
        
        return merged


# Example usage
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(s.merge([[1,4],[4,5]]))                 # Output: [[1,5]]
print(s.merge([[4,7],[1,4]]))                 # Output: [[1,7]]
