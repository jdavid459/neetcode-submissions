class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        cleaned_s = ''
        for c in s:
            if c.isalnum():
                cleaned_s += c
            else:
                pass
        print(cleaned_s)
        return cleaned_s == cleaned_s[::-1]

        # def reverseString(s: str) -> str:
        #     reversed_string = ''
        #     for c in range(len(s)-1,-1,-1):
        #         if s[c] == '':
        #             pass
        #         if s[c].isalnum():
        #             reversed_string += s[c]
        #         else:
        #             pass
        #         reversed_string = reversed_string.lower()
        #     return reversed_string
        # print(reverseString(s))


        # return s.lower == reverseString(s)
        