class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:

                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        while stack:

            height = heights[stack.pop()]

            width = len(heights) if not stack else len(heights) - stack[-1] - 1

            area = height * width

            max_area = max(max_area, area)

        return max_area