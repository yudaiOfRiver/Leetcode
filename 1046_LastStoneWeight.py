import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxheap = list(map(lambda x: -1*x, stones))
        heapq.heapify(maxheap)

        while len(maxheap) >= 2:
            y = heapq.heappop(maxheap)
            x = heapq.heappop(maxheap)
            x, y = -x, -y
            if x < y:
                heapq.heappush(maxheap, x-y)
        return maxheap[0] if maxheap else 0



