class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        curMin = [inf] * (amount + 1)   # set infinity ,including 0
        curMin[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    curMin[i] = min(curMin[i], 1+curMin[i-c])
        return curMin[amount] if curMin[amount] != inf else -1
