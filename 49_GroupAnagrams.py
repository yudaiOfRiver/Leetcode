from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                cnt[idx] += 1
            anagrams[tuple(cnt)].append(s)


        return list(anagrams.values())


strs = ["ddddddddddg","dgggggggggg"]
obj = Solution()
print(obj.groupAnagrams(strs))


