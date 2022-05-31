import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kMaxHeap = sorted(nums)[-k:]
        heapq.heapify(self.kMaxHeap)

    def add(self, val: int) -> int:
        if len(self.kMaxHeap) < self.k:
            heapq.heappush(self.kMaxHeap, val)
        elif val > self.kMaxHeap[0]:
            heapq.heappushpop(self.kMaxHeap, val)
        return self.kMaxHeap[0]
