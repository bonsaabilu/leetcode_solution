class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            # Double temp until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return sign * quotient
