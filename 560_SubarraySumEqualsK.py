from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        
        hash = defaultdict(lambda: 0)  # {prefix: count}
        hash[0] += 1
        sum = 0    # sum from index 0 to nums.index(c)
        for c in nums:
            sum += c
            if sum-k in hash.keys():
                res += hash[sum-k]
            hash[sum] += 1
        return res