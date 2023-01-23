# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    length = 1
    present = set()
    for r in range(0, len(s)):
        if s[r] in present:
            present.remove(s[r])
            l += 1
        present.add(s[r])
        length = max(length, r - l + 1)
    return length

    """
    Time - O(n)
    Space - O(n)
    """
        
