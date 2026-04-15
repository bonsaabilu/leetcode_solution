class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            # If we already have 4 parts
            if len(path) == 4:
                # If we used all characters, it's valid
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try taking 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Check for leading zero
                if len(part) > 1 and part[0] == '0':
                    continue

                # Check range
                if int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res