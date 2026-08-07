class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))    
        trees.sort()
        sr, sc = 0, 0
        total = 0
        for height, r, c in trees:
            steps = self.bfs(forest, sr, sc, r, c)
            if steps == -1:
                return -1
            total += steps
            sr, sc = r, c
        return total

    def bfs(self, forest, sr, sc, r, c):
        m = len(forest)
        n = len(forest[0])
        dr = (0, 0, -1, 1)
        dc = (-1, 1, 0, 0)
        if sr == r and sc == c:
            return 0
        queue = deque([(sr, sc, 0)])
        visited = {(sr, sc)}
        while queue:
            a, b, step = queue.popleft()
            for k in range(4):
                tr = a + dr[k]
                tc = b + dc[k]
                if (0 <= tr < m and 0 <= tc < n and forest[tr][tc] != 0 and (tr,tc) not in visited):
                    if tr == r and tc == c :
                        return step + 1
                    visited.add((tr, tc))
                    queue.append((tr, tc, step+1))
        return -1        



