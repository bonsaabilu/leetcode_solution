
class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        diagonals = set()
        anti_diagonals = set()

        def backtrack(row):

            if row == n:
                return 1

            count = 0

            for col in range(n):

                diagonal = row - col
                anti_diagonal = row + col

                if (col in cols or
                    diagonal in diagonals or
                    anti_diagonal in anti_diagonals):
                    continue

                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)

                count += backtrack(row + 1)

                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

            return count

        return backtrack(0)
