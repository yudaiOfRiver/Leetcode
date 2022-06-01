from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)    # {"*og" : dog, cog, "d*g" : dog, dig}
        wordList.append(beginWord)
        for word in wordList:      # O(nm) for n:len(wordList), m:len(beginWord)
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:     # O(n)
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):     # O(m)
                    pattern = cur[:j] + "*" + cur[j+1:]
                    for word in nei[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
            res += 1
        return 0
