class Solution:
    def reverse(self, x: int) -> int:
        # Handle the sign separately
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Convert to string, reverse it, convert back to int
        reversed_num = int(str(x)[::-1])
        
        # Put sign back
        result = sign * reversed_num
        
        # 32-bit integer range check
        if result > 2**31 - 1 or result < -2**31:
            return 0
            
        return result