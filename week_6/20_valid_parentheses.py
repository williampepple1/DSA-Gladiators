class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in range(len(s)):
            if s[i] in bracket.values():
                stack.append(s[i])
                continue

            if len(stack) != 0 and bracket[s[i]] == stack[-1]:
                stack.pop()
                continue

            else:
                return False

        return len(stack) == 0
