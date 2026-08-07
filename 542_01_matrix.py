class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)
        disc = [[-1] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    disc[i][j] = 0
                    queue.append((i, j))
                    
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if (0 <= x < m and 0 <= y < n and disc[x][y] < 0):
                    disc[x][y] = disc[a][b] + 1
                    queue.append((x, y))
        return disc
