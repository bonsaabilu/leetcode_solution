class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: negatives and numbers ending with 0 (except 0) → not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        # Step 2: reverse only half of the number
        reversed_half = 0
        
        # We only need to reverse until we reach the middle
        while x > reversed_half:
            # Take last digit and add to reversed_half
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            
            # Remove last digit from original number
            x = x // 10
        
        # Now compare:
        # even length: x should == reversed_half
        # odd length: x should == reversed_half // 10 (middle digit ignored)
        return x == reversed_half or x == reversed_half // 10