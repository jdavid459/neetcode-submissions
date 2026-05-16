class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        s_map = {}
        t_map = {}


        # caar
        # c: 1
        # a: 2
        # r: 1



        for c in s:
            s_map[c] = s_map.get(c,0) + 1

        for c in t:
            t_map[c] = t_map.get(c,0) + 1

        return s_map == t_map