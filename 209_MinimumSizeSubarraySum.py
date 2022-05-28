class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        curSum = 0
        curLength = 0

        for i in range(len(nums)):
            curSum += nums[i]
            curLength += 1
            j = i - curLength + 1
            while curSum >= target:
                res = min(res, curLength)
                print(res, curSum, j)
                curSum -= nums[j]
                curLength -= 1
                j += 1

        return res if res != float('inf') else 0
