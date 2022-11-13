class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        not_captured = set()

        def dfs(r, c):
            visited.add((r, c))
            not_captured.add((r, c))

            directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if (rr in range(ROWS)) and (cc in range(COLS)) and (rr, cc) not in visited:
                    if (board[rr][cc] == 'O'):
                        dfs(rr ,cc)


        for row in range(ROWS):
            if row == 0 or row == (ROWS-1):
                for col in range(COLS):
                    if board[row][col] == 'O':
                        dfs(row, col)
            else:
                if board[row][0] == 'O':
                    dfs(row, 0)
                if board[row][COLS-1] == 'O':
                    dfs(row, COLS-1)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in not_captured:
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'



