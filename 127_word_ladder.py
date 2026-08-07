class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList_set = set(wordList)
        if endWord not in wordList_set:
            return 0
        queue = deque([beginWord])
        visited = {beginWord}
        word = 1
        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.popleft()
                if cur == endWord:
                    return word
                
                for pos in range(len(cur)):
                    for k in range(26):
                        if cur[pos] != chr(k + ord('a')):
                            wordList = list(cur)
                            wordList[pos] = chr(k + ord('a'))
                            new_wlist = "".join(wordList)
                            if new_wlist in wordList_set and new_wlist not in visited:
                                visited.add(new_wlist)
                                queue.append(new_wlist)
            word += 1
        return 0
        
        """
        注意if new_wlist in wordList_set and new_wlist not in visited:主语要有 X not in Y
        chr(k + ord('a'))
        """
        