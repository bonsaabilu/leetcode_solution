class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        # Initialize
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + c//3].add(val)
        
        def backtrack(i):
            if i == len(empty):
                return True
            
            r, c = empty[i]
            box = (r//3)*3 + c//3
            
            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    
                    # Place
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)
                    
                    if backtrack(i + 1):
                        return True
                    
                    # Undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)
            
            return False
        
        backtrack(0)