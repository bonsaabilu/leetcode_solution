class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # stores last index of each character
        left = 0          # left pointer of sliding window
        max_len = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1  # move left pointer

            char_index[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
