class Solution(object):
    def twoSum(self, nums, target):                                                               
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}   # {difference between index i and target: i}
        for i in range(len(nums)):
            if target-nums[i] in hash.keys():
                return [i, hash[target-nums[i]]]
            else:
                hash[nums[i]] = i