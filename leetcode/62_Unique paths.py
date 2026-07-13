class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1 ) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]



        """
        创建二维列表
        dp = ([0]*n for _ in range(m))
        for循环是循环每一行时每一列都要循环，先从j列循环完再跳出来继续循环i重新循环行。
        dp是用来计算每一个格子的值最后给返回值使用的
        """
