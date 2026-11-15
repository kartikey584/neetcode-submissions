class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        lookup = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        if s[0] in lookup.keys():
            return False

        for i in s:
            if i in lookup.values():
                stack.append(i)
            elif stack and stack[-1] == lookup[i]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False
        