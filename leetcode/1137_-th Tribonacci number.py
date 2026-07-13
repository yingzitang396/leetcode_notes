class Solution:
    def tribonacci(self, n: int) -> int:
        # 创建dp表
        # 初始化
        # 填表
        # 返回值return
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]




        """
        一个数 range(n)：0 到 n-1
        两个数 range(a, b)：a 到 b-1
        三个数 range(a, b, step)：a 开始，每次跳 step，到 b 之前停
        永远记住：终点不包含，想包含就 +1
        列表创建：
        这是一个很容易踩的坑：[] * 5 结果是 []，不是 [None, None, None, None, None]。
        因为空列表里没有东西可以重复，乘多少次都还是空的。
        你想要的效果应该是创建一个长度为 n+1 的列表，先用占位符填满：
        
        
        
        DP： i格子的值以什么为开头或者以什么为结束
        """