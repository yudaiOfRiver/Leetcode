class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        inf = float('inf')
        DP = [inf] * n
        DP[-1] = 0

        for i in range(n-2, -1, -1): # 最後から2番目から逆順
            if nums[i] == 0:
                continue
            limit_j = min(i + nums[i], n-1)
            DP[i] = 1 + min(DP[j] for j in range(i+1, limit_j+1))

        return DP[0]


nums = [2,3,0,1,4]
obj = Solution()
print(obj.jump(nums))



