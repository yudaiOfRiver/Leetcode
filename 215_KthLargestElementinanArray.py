import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = map(lambda x: -x, nums)

        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, n)

        for i in range(k):
            ith = heapq.heappop(maxHeap)
        return -ith


