class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        n = list(sorted(set(nums)))
        out = [n[0]]
        result = 0
        for i in range(1,len(n)):
            if out[-1] == n[i] - 1:
                out.append(n[i])
            else:
                if result < len(out):
                    result = len(out)
                out = [n[i]]
        if result < len(out):
            result = len(out)
        return result

