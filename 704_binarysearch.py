class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m-1
            elif nums[m] < target:
                l = m+1
        return -1

nums = [-1,0,3,5,9,12]
target = 8
## Output: 4

obj = Solution()
print(obj.search(nums, target))
