from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        cnt = defaultdict(lambda: 0)
        for n in nums:
            if cnt[n] == 1:
                return True
            else:
                cnt[n] += 1
        return False

