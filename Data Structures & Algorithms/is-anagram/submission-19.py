class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter_counts_s = {}
        letter_counts_t = {}

        for c in s:
            letter_counts_s[c] = letter_counts_s.get(c,0) + 1
        
        for c in t:
            letter_counts_t[c] = letter_counts_t.get(c,0) + 1
        
        # print(letter_counts_s)
        # print(letter_counts_t)

        return letter_counts_s == letter_counts_t