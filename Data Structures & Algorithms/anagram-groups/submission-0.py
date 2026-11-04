class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = defaultdict(list)

        for i in strs:

            key = ''.join(sorted(i))
            out[key].append(i)

        return list(out.values())