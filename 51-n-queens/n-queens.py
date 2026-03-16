class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0, results, n)
        return results

    def backtrack(self, board, row, results, n):
        if row == n:
            # Convert board to list of strings
            solution = ["".join(r) for r in board]
            results.append(solution)
            return
        for col in range(n):
            if not self.isSafe(board, row, col, n):
                continue
            board[row][col] = "Q"
            self.backtrack(board, row + 1, results, n)
            board[row][col] = "."

    def isSafe(self, board, row, col, n):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True


# Example usage
s = Solution()
print(s.solveNQueens(4))
# Output: [[".Q..","...Q","Q...","..Q."],
#          ["..Q.","Q...","...Q",".Q.."]]

print(s.solveNQueens(1))
# Output: [["Q"]]
