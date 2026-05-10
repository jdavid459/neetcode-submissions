class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        
        j = 0
        for i, c in enumerate(s):
            if c not in t:
                return False
            # elif t[c] < j:
            #     return False
            # j = t[c]
            idx = t.find(c, j)

            if idx == -1:
                return False

            j = idx + 1
        return True

            
        