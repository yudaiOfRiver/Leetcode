class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        myHeap = []
        
        for i in range(len(nums1)):
            heapq.heappush(myHeap,(nums1[i] + nums2[0], i, 0))
            
        res = []
        #print(myHeap)
        while k > 0 and myHeap:
            _, i, j = heapq.heappop(myHeap)
            res.append([nums1[i],nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(myHeap, (nums1[i] + nums2[j+1], i, j+1))
                print([i, j+1])
            k -= 1
        return res        