class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # If the current string is complete
            if len(current) == 2 * n:
                res.append(current)
                return
            
            # Add '(' if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add ')' if it won't break validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res

 