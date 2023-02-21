class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = list(s)
        stack = []

        for i in range(len(valid)):
            if valid[i] == "(":
                stack.append(i)
            elif valid[i] == ")":
                if stack:
                    stack.pop()
                else:
                    valid[i] = ""

        for j in stack:
            valid[j] = ""

        return "".join(valid)
