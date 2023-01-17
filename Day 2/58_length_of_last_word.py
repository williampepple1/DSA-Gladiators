# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split(' ')[-1])

        """
        Alternate Solution
        s = s.strip()
        length = len(s) - 1
        for i in range(length, -1, -1):
            if s[i] == ' ':
                return length - i
        return len(s)
        """
