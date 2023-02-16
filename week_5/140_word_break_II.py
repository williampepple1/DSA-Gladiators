"""Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is 
a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Link: https://leetcode.com/problems/word-break-ii/

N.B: Fom the input, go ahead to define your method and argument(s) you suggest it should take.

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memoDict = {}
        return self.helper(s, wordSet, memoDict)

    def helper(self, w, wordSet, memoDict):
        result = []
        if w in memoDict:
            return memoDict[w]

        for i in range(len(w)):
            prefix = w[:i + 1]
            suffix = w[i + 1:]

            if prefix in wordSet:
                if prefix == w:
                    result.append(prefix)
                else:
                    restOfWord = self.helper(suffix, wordSet, memoDict)
                    for word in restOfWord:
                        result.append(prefix + " " + word)
                memoDict[w] = result

        return result
