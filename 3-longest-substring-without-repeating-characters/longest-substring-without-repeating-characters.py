class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # stores the last index of each character
        left = 0          # left pointer of the sliding window
        max_len = 0

        for right, ch in enumerate(s):
            # If character is already in window, move left pointer
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            # Update the last index of the character
            char_index[ch] = right

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
