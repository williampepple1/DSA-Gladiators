# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        start = 0
        length = 0

        for i in range(len(s)):
            if s[i] in store and start <= store[s[i]]:
                start = store[s[i]] + 1

            length = max(length, (i - start) + 1)
            store[s[i]] = i

        return length

        