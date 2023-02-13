def removeDuplicates(s, k):
    stack = []
    for i in range(len(s)):
        if stack and s[i] == stack[-1][0]:
            if stack[-1][1] + 1 == k:
                stack.pop()
            else:
                stack[-1][1] += 1
        else:
            stack.append((s[i], 1))

    return "".join(i * c for i, c in stack)