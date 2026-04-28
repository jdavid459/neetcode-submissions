class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar
        # aaccerr
        # carrace
        # aaccerr

        #time -> n to sort
        #space -> no new objects, O1/constant?

        return ''.join(sorted(s)) == ''.join(sorted(t[::-1]))
        