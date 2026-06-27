class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_len = 0

        for c in s:
            if c in substring:
                substring = substring[substring.index(c) + 1:]
            substring += c
            max_len = max(max_len, len(substring))
        return max_len

        # for i, c in enumerate(s):
        #     if c not in substring:
        #         substring += c
        #     elif c in substring or i == len(s)-1:
        #         if len(substring) > max_len:
        #             max_len = len(substring)
        #         substring = c
        # return max_len

        