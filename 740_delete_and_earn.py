class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 建立一个arr的映射表
        max_value = max(nums)
        arr = [0] * (max_value + 1)
        for i in nums:
            arr[i] += i
        # 建立dp表
        f = [0] * (max_value + 1)  
        g = [0] * (max_value + 1) 
        # 初始化
        f[0] = arr[0]
        g[0] = 0
        # 填表
        for i in range(max_value+1):
            f[i] = g[i-1] + arr[i]
            g[i] = max(f[i-1], g[i-1])
        # 返回值
        return max(f[max_value], g[max_value])


# 在arr表格里面进行一次打家劫舍的套用
# 学到了如何找到list里面的最大值
