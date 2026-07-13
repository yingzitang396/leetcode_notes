class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # dp = []
        # for k in range(m):
        #     dp.append([float('inf')] * (n+2))
        dp = [[float('inf')] * (n+2) for _ in range(m)]
        for i in range(1, n+1):
            dp[0][i] = matrix[0][i-1]
        for i in range(1, m):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + matrix[i][j-1]
        ret = float('inf')
        for i in range(1, n+1):
            ret = min(ret,dp[m-1][i])
        return ret    