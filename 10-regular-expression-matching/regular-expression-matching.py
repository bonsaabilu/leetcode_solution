class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m = length of string s, n = length of pattern p
        m, n = len(s), len(p)
        
        # dp[i][j] = true if first i chars of s match first j chars of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Empty string can match patterns like a*, a*b*, etc.
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # '*' can match zero occurrences → look at previous previous state
                dp[0][j] = dp[0][j-2]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current characters
                char_s = s[i-1]
                char_p = p[j-1]
                
                if char_p == '.' or char_p == char_s:
                    # Normal match or '.' match → take diagonal (previous states)
                    dp[i][j] = dp[i-1][j-1]
                
                elif char_p == '*':
                    # Two choices for '*':
                    # 1. Use * to match zero times → ignore this 'x*' pair
                    zero_times = dp[i][j-2]
                    
                    # 2. Use * to match one or more times → if previous char matches
                    one_or_more = dp[i-1][j] and (p[j-2] == '.' or p[j-2] == char_s)
                    
                    dp[i][j] = zero_times or one_or_more
        
        # Answer is whether whole string matches whole pattern
        return dp[m][n]