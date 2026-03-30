class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)   # Faster lookup
        n = len(s)
        
        # dp[i] means: can s[:i] be segmented?
        dp = [False] * (n + 1)
        dp[0] = True   # Empty string is always segmentable
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break   # No need to check further
        
        return dp[n]
