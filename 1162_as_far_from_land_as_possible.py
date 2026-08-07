class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    visited[i][j] = True
                    queue.append((i, j))
        ret = 0
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if(0 <= x < m and 0 <= y < n and grid[x][y]== 0 and not visited[x][y]):
                    grid[x][y] = grid[a][b] + 1
                    ret = max(ret, grid[x][y])
                    visited[x][y] = True
                    queue.append((x, y))
        if ret == 0:
            return -1
        return ret

