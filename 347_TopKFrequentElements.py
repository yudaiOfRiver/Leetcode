from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)  # {element: frequency}
        reverseLookUp = defaultdict(list)  # {frequency: [ element1, elements2 ]}

        for num in nums:
            freq[num] += 1

        for el, fr in freq.items():
            reverseLookUp[fr].append(el)

        res = []
        while len(res) < k:
            val = reverseLookUp.pop(max(list(reverseLookUp.keys())))
            res.extend(val)

        return res


