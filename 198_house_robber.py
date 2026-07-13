class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        g = [0] * n
        f[0] = nums[0]
        g[0] = 0
        for i in range(1, n):
            f[i] = g[i-1] + nums[i]
            g[i] = max(f[i-1], g[i-1])
        return max(g[n-1], f[n-1])

