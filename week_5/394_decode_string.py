"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated 
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are
well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are
only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Link: https://leetcode.com/problems/decode-string/

N.B: Fom the input, go ahead to define your method and argument(s) you suggest it should take.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string, cur_num = "", 0
        for c in s:
            if c == "[":
                stack.append(cur_num)
                stack.append(cur_string)
                cur_string, cur_num = "", 0
            elif c == "]":
                char = stack.pop()
                num = stack.pop()
                cur_string = char + num * cur_string
            elif c.isdigit():
                cur_num = int(c) + 10 * cur_num
            else:
                cur_string += c
        return cur_string
