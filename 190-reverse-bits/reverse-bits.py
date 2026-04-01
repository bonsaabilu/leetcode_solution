class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  # iterate over all 32 bits
            # Shift result left to make room
            result <<= 1
            # Add the least significant bit of n
            result |= (n & 1)
            # Shift n right to process next bit
            n >>= 1
        return result
