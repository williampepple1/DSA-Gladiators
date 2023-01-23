# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ## Time - O(n)
        ## Space - O(1)

        lastLength = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if lastLength > 0:
                    return lastLength
            else:
                lastLength += 1
        
        return lastLength