class Solution:
    def findMin(self, nums: List[int]) -> int:

        l ,r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > nums[len(nums)-1]:
                l = m+1
            elif nums[m] <= nums[len(nums)-1]:
                print(m)
                if m == 0:
                    return nums[m]
                if m > 0 and nums[m-1] > nums[m]:
                    return nums[m]
                r = m-1

