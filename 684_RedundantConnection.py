class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]] # 効率性の観点から、1個飛ばしで親までたどる
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

        for n1, n2 in edges:
            if find(n1) == find(n2):
                return [n1, n2]
            union(n1, n2)




edges = [[1,2],[1,3],[2,3]]
obj = Solution()
print(obj.findRedundantConnection(edges))
