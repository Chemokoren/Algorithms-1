from typing import List
"""
Topological sort(DAG): 

There is a new alien language that uses the English alphabet. However, the order among the
letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the 
strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically 
increasing order by the new language's rules. If there is no solution, return "". 
If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they 
differ, the letter in s comes before the letter in t in the alien language. If the first 
min(s.length, t.length) letters are the same, then s is smaller if and only 
if s.length < t.length

Example 1 :

    Input: words =["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

"""
class Solution:
    
    def alienOrder(self, words: List[str])->str:
        adj ={c:set() for w in words for c in w}

        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen =min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] ==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit ={} # False=visited, True= visited & in Path
        res =[]

        # post order dfs
        def dfs(c):
            if c in visit: # means we have detected a loop
                return visit[c]# it has not only been visited but it is also in the current path

            visit[c] =True
            for nei in adj[c]:
                if dfs(nei):
                    return True # loop has been detected
            visit[c] =False
            res.append(c)
        for c in adj:
            if dfs(c):
                return "" # we detected a loop
        res.reverse()
        return "".join(res)

words =["wrt","wrf","er","ett","rftt"]
sol = Solution()
print(sol.alienOrder(words))