class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Reduce the prefix length until it matches the start of string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove the last character
                if not prefix:
                    return ""  # no common prefix
        
        return prefix
        