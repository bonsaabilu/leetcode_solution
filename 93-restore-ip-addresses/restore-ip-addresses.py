class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.backtrack(s, 0, [], result)
        return result

    def backtrack(self, s, start, path, result):
        # If we already have 4 parts and consumed all digits → valid IP
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Try segments of length 1 to 3
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]

            # Skip invalid segments: leading zeros or >255
            if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                continue

            path.append(segment)
            self.backtrack(s, start + length, path, result)
            path.pop()


# Example usage
s = Solution()
print(s.restoreIpAddresses("25525511135"))
# Output: ["255.255.11.135","255.255.111.35"]

print(s.restoreIpAddresses("0000"))
# Output: ["0.0.0.0"]

print(s.restoreIpAddresses("101023"))
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
