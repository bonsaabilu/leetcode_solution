
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine the sign
        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read digits and build the number
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        # 4. Apply the sign
        num *= sign

        # 5. Clamp to the 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num
