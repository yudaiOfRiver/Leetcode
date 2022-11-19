class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = max(i + nums[i] for i in range(l, r+1))
            l, r = r+1, farthest
            res += 1

        return res



nums = [2,3,0,1,4]
obj = Solution()
print(obj.jump(nums))



