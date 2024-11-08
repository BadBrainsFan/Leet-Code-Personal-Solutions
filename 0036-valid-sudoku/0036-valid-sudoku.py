class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for colum in range(9):
                if board[row][colum] == ".":
                    continue
                if (board[row][colum] in rows[row] or
                    board[row][colum] in colums[colum] or
                    board[row][colum] in squares[(row//3, colum//3)]):
                    return False
                colums[colum].add(board[row][colum])
                rows[row].add(board[row][colum])
                squares[(row//3, colum//3)].add(board[row][colum])
        return True