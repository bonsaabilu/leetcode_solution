class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # store last seen position of characters
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If character already exists and is inside current window
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # move left pointer

            # Update last seen position
            char_index[s[right]] = right

            # Calculate window length
            max_length = max(max_length, right - left + 1)

        return max_length
        