class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        result = 0
        prev_r = 0

        while left < right and left != right:

            w = right - left
            h = min(heights[left],heights[right])

            if result < w * h:
                result = w * h
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result