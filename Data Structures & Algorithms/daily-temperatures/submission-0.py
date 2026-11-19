class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        suf = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                prev = stack.pop()
                suf[prev] = i - prev

            stack.append(i)

        return suf
