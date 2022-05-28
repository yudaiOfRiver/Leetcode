class Solution(object):
    def isPalindrome(self,x) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

#obj = Solution()
#obj.isPalindrome(1221)

