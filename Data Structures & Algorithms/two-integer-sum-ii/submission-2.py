class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        check = {}

        for i,value in enumerate(numbers):
            left = target - value

            if left in check.keys():
                return sorted([i+1,check[left]+1])
            check[value] = i