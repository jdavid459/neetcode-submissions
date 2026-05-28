class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s_clean = ''
        for c in s:
            if c.isalnum():
                s_clean += c
        l, r = 0, len(s_clean)-1
        

        

        while l < r:
            if s_clean[l] == s_clean[r]:
                l += 1
                r -= 1
            else:
                return False
        return True




        