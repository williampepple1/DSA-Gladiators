# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substringSet = set()

        left, right = 0, 0

        while right < len(s):
            while s[right] in substringSet:
                substringSet.remove(s[left])
                left += 1

            substringSet.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
