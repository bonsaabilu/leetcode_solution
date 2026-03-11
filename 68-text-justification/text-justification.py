class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: Greedily fit as many words as possible into the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # Step 2: Build the line
            line_words = words[i:j]
            num_words = j - i

            # Case A: Last line OR only one word in the line → left-justified
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Case B: Fully justified line
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                line = ""
                for k in range(num_words - 1):
                    line += line_words[k]
                    # Add evenly distributed spaces
                    line += " " * (space_between + (1 if k < extra_spaces else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res
