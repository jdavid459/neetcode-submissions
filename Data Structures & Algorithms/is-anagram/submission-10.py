class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}
        n = {}

        for c in s:
            m[c] = m.get(c, 0) + 1

        for c in t:
            n[c] = n.get(c, 0) + 1

        return m == n



        