class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # This dictionary will store the groups of anagrams.
        #
        # The key will be the sorted version of a word.
        # The value will be a list of words that match that sorted version.
        #
        # Example:
        # "eat" -> "aet"
        # "tea" -> "aet"
        # So both go under the same key: "aet"
        groups = {}

        # Look at each word in the input list
        for word in strs:

            # Sort the letters in the word.
            #
            # sorted(word) turns the word into a sorted list of characters.
            # Example:
            # sorted("eat") -> ["a", "e", "t"]
            #
            # ''.join(...) turns that list back into a string.
            # Example:
            # ''.join(["a", "e", "t"]) -> "aet"
            sorted_word = ''.join(sorted(word))

            # If this sorted version has not been seen before,
            # create a new empty list for this anagram group.
            if sorted_word not in groups:
                groups[sorted_word] = []

            # Add the original word to the correct anagram group.
            #
            # Example:
            # groups["aet"].append("eat")
            # groups["aet"].append("tea")
            groups[sorted_word].append(word)

        # groups is a dictionary, but the problem wants a list of lists.
        #
        # Example:
        # {
        #   "aet": ["eat", "tea", "ate"],
        #   "ant": ["tan", "nat"],
        #   "abt": ["bat"]
        # }
        #
        # groups.values() gives:
        # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        return list(groups.values())