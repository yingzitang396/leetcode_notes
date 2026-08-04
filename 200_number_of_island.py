class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.bfs(grid, visited, i, j, m, n)
        return count

    def bfs(self, grid, visited, i, j, m, n):
        queue = deque([(i, j)])
        visited[i][j] = True

        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < m and 0 <= ny < n
                        and grid[nx][ny] == '1'
                        and not visited[nx][ny]):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        