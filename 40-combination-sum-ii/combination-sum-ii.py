class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # sort to handle duplicates easily
        res = []

        def backtrack(start: int, path: list[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res
