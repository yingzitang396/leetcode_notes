class Solution:
    def numDecodings(self, s: str) -> int: #1
        # 创建dp表
        # 填表
        # 初始化
        #填表
        n = len(s)
        dp = [0] * n
        if int(s[0]) == 0:
            return 0
        else:
            dp[0] = 1
        if n == 1:
            return dp[0]
        if int(s[1]) != 0:
            dp[1] += 1
        if int(s[0])*10 + int(s[1]) >= 10 and int(s[0])*10 + int(s[1]) <=26:
            dp[1] += 1
        for i in range(2,n):
            if int(s[i])!= 0:
                dp[i] += dp[i-1]
            if int(s[i-1]) * 10 + int(s[i]) >=10 and int(s[i-1]) * 10 + int(s[i]) <=26:
                dp[i] += dp[i-2] 
        return dp[n-1]        



        

        