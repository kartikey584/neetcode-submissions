class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left_m = 0
        right_m = len(matrix) - 1

        while left_m <= right_m:

            mid = (left_m + right_m) // 2
            if target in matrix[mid]:
                return True
            elif target > matrix[mid][-1]:
                left_m = mid + 1
            else:
                right_m = mid - 1
        return False