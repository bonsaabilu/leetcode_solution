class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        return self.fastPow(x, n)

    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


# Example usage in Python 2
s = Solution()
print(s.myPow(2.00000, 10))   # Output: 1024.0
print(s.myPow(2.10000, 3))    # Output: 9.261
print(s.myPow(2.00000, -2))   # Output: 0.25

