class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        return self.dfs(A, B, C)
    
    def dfs(self, n, start, middle, last,):
        if n == 1:
            last.append(start.pop())
        self.dfs(n-1, start, last, middle)
        last.append(start.pop())
        self.dfs(n-1, middle, start, last)