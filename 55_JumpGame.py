class Solution:
    def canJump(self, nums: list[int]) -> bool:

        zero_idx = 'No' # the last index of zero currently
        for i in range(len(nums)-1, -1, -1):
            if (i != len(nums)-1) and (nums[i] == 0) and zero_idx == 'No':
                zero_idx = i
            elif (zero_idx != 'No'):
                if(nums[i] > zero_idx - i):
                    zero_idx = 'No'

        if zero_idx == 'No':
            return True
        else:
            return False


nums = [2,0,1,0,1]
obj = Solution()
print(obj.canJump(nums))

