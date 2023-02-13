def removeDuplicates(s: str, k: int) -> str:
    stack = []

    for character in s:
        if stack and stack[-1][0] == character:
            stack[-1][1] += 1

        else:
            stack.append([character, 1])

        if stack[-1][1] == k:
            stack.pop()

    result = ""

    for character, count in stack:
        result += character * count

    return result
