class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        for s in strs:
            # Sort each string to form the key
            key = ''.join(sorted(s))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
        return anagram_map.values()


# Example usage in Python 2
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

print(s.groupAnagrams([""]))
# Output: [[""]]

print(s.groupAnagrams(["a"]))
# Output: [["a"]]
