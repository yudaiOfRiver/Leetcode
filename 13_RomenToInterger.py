class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'Z': 0,  # prevent over index
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50, 
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s + "Z" 
        result = 0
        
        for i in range(len(s)):
            if dict[s[i]] >= dict[s[i+1]]:
                result += dict[s[i]]
            else:
                result -= dict[s[i]]
        return result

#obj = Solution()
#print(obj.romanToInt("III"))
#print(obj.romanToInt("LVIII"))
#print(obj.romanToInt("MCMXCIV"))

