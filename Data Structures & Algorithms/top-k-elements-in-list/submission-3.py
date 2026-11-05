class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = dict(sorted(Counter(nums).items(), key=lambda item: item[1]))

        return list(c.keys())[-k:]

