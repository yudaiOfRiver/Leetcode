class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def houseRobber1(numlist):
            if len(numlist) == 1:
                return numlist[0]

            curSum = [0 for _ in range(len(numlist))]
            for i in range(len(numlist)):
                if i == 0:
                    curSum[i] = numlist[i]
                elif i == 1:
                    curSum[i] = max(numlist[i], curSum[i-1])
                else:
                    curSum[i] = max(curSum[i-1], curSum[i-2] + numlist[i])
            return curSum[-1]

        return max(houseRobber1(nums[:-1]), houseRobber1(nums[1:]))
