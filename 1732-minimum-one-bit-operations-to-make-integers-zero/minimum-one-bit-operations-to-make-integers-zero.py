class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = n
        while n:
            n >>= 1
            res ^= n
        return res