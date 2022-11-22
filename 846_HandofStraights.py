class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) == 1:
            return True

        def hasStraight(n):
            for i in range(1, groupSize):
                if n+i not in hand:
                    return False
            return True

        hand.sort()
        cur = hand.pop(0)
        while hasStraight(cur):
            for i in range(1, groupSize):
                hand.remove(cur+i)

            if not hand:
                return True
            cur = hand.pop(0)

        return False

hand = [1,2,3,4,5,6]
groupSize = 2
obj = Solution()
print(obj.isNStraightHand(hand, groupSize))
