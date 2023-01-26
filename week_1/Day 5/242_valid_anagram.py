# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = {}

        for i in range(len(s)):
            char_dict[s[i]] = char_dict.get(s[i], 0) + 1
            char_dict[t[i]] = char_dict.get(t[i], 0) - 1

        for idx in char_dict.values():
            if idx != 0:
                return False
        return True

        