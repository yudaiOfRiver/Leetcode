class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        parent = self.kthGrammar(n-1, k//2 + k%2)  # round-up  ex) 3//2 + 3%2 = 2, 8//2 + 8%2 = 4
        isKOdd = (k%2 == 1)

        if parent == 0:
            return 0 if isKOdd else 1
        else:
            return 1 if isKOdd else 0








