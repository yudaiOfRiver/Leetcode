class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        idx = dict()

        for i in range(N):
            ni = nums[i]
            if idx.get(target-ni, -1) != -1 and idx.get(target-ni, -1) != i:
                return [i, idx[target-ni]]
            else:
                idx[ni] = i

nums = [3,2,4]
target = 6
obj = Solution()
print(obj.twoSum(nums, target))
