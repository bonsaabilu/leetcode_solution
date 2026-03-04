class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
            
        # Handle sign
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
            
        # Read only digits
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)
            
            # Cap at 32-bit limits
            if num >= 2**31:
                return 2**31 - 1 if sign == 1 else -2**31
        
        return sign * num
        