import heapq
from collections import deque
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = Counter(tasks)
        maxHeap = []
        for cnt in c.values():
            heapq.heappush(maxHeap, -cnt)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                reuse, _ = q.popleft()
                heapq.heappush(maxHeap, reuse)

        return time


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

obj = Solution()
print(obj.leastInterval(tasks, n))




