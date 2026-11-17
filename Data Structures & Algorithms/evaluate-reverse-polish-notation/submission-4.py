class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i,val in enumerate(tokens):

            if val not in ['+','-','*','/']:
                stack.append(int(val))
            elif val == '+':
                ans = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif val == '*':
                ans = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif val == '-':
                ans = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif val == '/':
                ans = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ans)
            # print(stack)
        return stack[-1]