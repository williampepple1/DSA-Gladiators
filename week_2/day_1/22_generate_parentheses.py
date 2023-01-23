"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parenthesis = []
        allParentheses = []

        def backtrack(o, c):
            if not o and not c:
                allParentheses.append("".join(parenthesis))
                return

            if o:
                parenthesis.append("(")
                backtrack(o - 1, c)
                parenthesis.pop()

            if c > o:
                parenthesis.append(")")
                backtrack(o, c - 1)
                parenthesis.pop()

            return

        backtrack(n, n)
        return allParentheses
