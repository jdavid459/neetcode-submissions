class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = ''
        for i in range(0,len(strs[0])):
            current_letter = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != current_letter:
                    return longest_prefix
                
            longest_prefix += current_letter
        return longest_prefix


