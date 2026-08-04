class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    self.bfs(board, i, j, m, n)
        
        for a in range(m):
            for b in range(n):
                if board[a][b] == '#':
                    board[a][b] = 'O'
                elif board[a][b] == 'O':
                    board[a][b] = 'X'


    def bfs(self, board, i, j, m, n):
        queue = deque([(i,j)])
        board[i][j] = '#'

        dx = (1, -1, 0, 0)
        dy = (0, 0, -1, 1)

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < m and 0 <= ny < n
                        and board[nx][ny] == 'O'):
                    board[nx][ny] = '#'
                    queue.append((nx, ny))

                
        