class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        best = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            best = max(best, right-left + 1)
        return best

        # substring = ''
        # max_len = 0

        # for c in s:
        #     if c in substring:
        #         substring = substring[substring.index(c) + 1:]
        #     substring += c
        #     max_len = max(max_len, len(substring))
        # return max_len

        # for i, c in enumerate(s):
        #     if c not in substring:
        #         substring += c
        #     elif c in substring or i == len(s)-1:
        #         if len(substring) > max_len:
        #             max_len = len(substring)
        #         substring = c
        # return max_len

        