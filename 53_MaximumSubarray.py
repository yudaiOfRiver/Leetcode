class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curMax = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            curMax = max(curMax, curSum)

        return curMax

nums = [-2,-1,-3,-1,-5]
obj = Solution()
print(obj.maxSubArray(nums))
