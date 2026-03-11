class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces, then split by spaces
        words = s.strip().split()
        # Return length of the last word
        return len(words[-1])
