import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = []
        dis_idx= defaultdict(list)

        for i, [x, y] in enumerate(points):
            dis = x**2 + y**2
            heapq.heappush(distance, dis)
            dis_idx[dis].append(i)

        res = []
        while len(res) < k:
            ithmin = heapq.heappop(distance)
            for ithidx in dis_idx[ithmin]:
                res.append(points[ithidx])
        return res

