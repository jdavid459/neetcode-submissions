class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_of_abs = 0
        for i in range(len(s)-1):
            sum_of_abs += abs(ord(s[i])-ord(s[i+1]))
        return sum_of_abs