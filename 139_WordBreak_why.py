class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possibility = [False for _ in range((len(s)+1))]
        possibility[-1] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                print(i, w)
                if i + len(w) in range(len(s)+1):
                    print(s[i:i+len(w)])
                    if s[i:i+len(w)] == w and possibility[i+len(w)] == True:
                        possibility[i] = True
                print(possibility)
        return possibility[0]

