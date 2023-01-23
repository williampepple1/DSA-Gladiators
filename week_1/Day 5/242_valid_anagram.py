# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       from collections import Counter
       return Counter(s) == Counter(t)

   """
   Time - O(n)
   Space - O(n)
   """
