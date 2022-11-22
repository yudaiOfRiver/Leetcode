from collections import defaultdict

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        t0, t1, t2 = target[0], target[1], target[2]

        has_ele = {t0: [], t1: [], t2: []}
        for i,[a, b, c] in enumerate(triplets):
            if a == t0 and b <= t1 and c <= t2:
                has_ele[t0].append(i)
            if a <= t0 and b == t1 and c <= t2:
                has_ele[t1].append(i)
            if a <= t0 and b <= t1 and c == t2:
                has_ele[t2].append(i)
        print(has_ele)

        for ti in [t0, t1, t2]:
            if has_ele[ti] == []:
                return False
        return True

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
obj = Solution()
print(obj.mergeTriplets(triplets, target))



