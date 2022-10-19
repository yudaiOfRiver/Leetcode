class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n: m, n = n, m
        num, den = 1, 1
        for i in range(n-1):
            num = num * (m+n-2-i)
            den = den * (n-1-i)
        return int(num/den)