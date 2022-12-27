"""
Alien dictionary
there is a new alien language that uses the english alphabet, however, the order among the letters is unknown to you. you are given a list of strings words,
from the alien language's dictionary where the strings in words are sorted lexicographically by the rules of this new language
return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules
if there is no solution, return "" if there are multiple solutions return any of them a string s is lexicographically smaller than a string t if at the first
letter where they differ the letter in s comes before the letter in t in the alien language if the first min(s.length,t.length) letters are the same,
then s is smaller if and only if s.length < t.length

Example 1:
    input: words = ["wrt","wrf","er","ett","rftt"]
    output: "wertf"
"""


class Solution:
    def alienDictionary(self, words):
        adj = {c: set() for w in words for c in w}
        print(adj)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}  # False=visited, True = visited and in current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return True
        res.reverse()
        return "".join(res)


wordsgot = ["wrt", "wrf", "er", "ett", "rftt"]
sol = Solution()
print(sol.alienDictionary(words=wordsgot))
