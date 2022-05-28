class Solution:
    def rob(self, nums: List[int]) -> int:
        curSum = collections.defaultdict(lambda: 0)
        for i in range(len(nums)):
            if i == 0:
                curSum[i] = nums[i]
            if i == 1:
                curSum[i] = max(nums[i], nums[i-1])
            else:
                curSum[i] = max(curSum[i-1], curSum[i-2] + nums[i])
        return curSum[-1]
