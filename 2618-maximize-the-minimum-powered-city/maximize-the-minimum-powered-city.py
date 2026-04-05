from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Step 1: Compute initial power using prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[i] = prefix[right + 1] - prefix[left]
        
        # Step 2: Check function (can we achieve at least 'target'?)
        def can(target):
            added = [0] * n
            curr_add = 0
            used = 0
            
            window_sum = 0
            j = 0
            
            for i in range(n):
                # Maintain sliding window sum
                if i - r - 1 >= 0:
                    window_sum -= added[i - r - 1]
                if i + r < n:
                    window_sum += added[i + r]
                
                total = power[i] + window_sum
                
                if total < target:
                    need = target - total
                    used += need
                    if used > k:
                        return False
                    
                    pos = min(n - 1, i + r)
                    added[pos] += need
                    window_sum += need
            
            return True
        
        # Step 3: Binary search
        left, right = 0, max(power) + k
        
        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1
        
        return left