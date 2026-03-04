class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
            
        # Convert to string and compare with its reverse
        s = str(x)
        return s == s[::-1]