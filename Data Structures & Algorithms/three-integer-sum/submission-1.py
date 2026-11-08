class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i + j = -k
        check = defaultdict()
        out = []
        for index_k,k  in enumerate(nums):
            check[k] = index_k
            for index_j,j in enumerate(nums):
                if index_j != index_k:
                    i = -k - j
                    if i in check.keys() and sorted([i,j,k]) not in out:
                        if check[i] != index_j and check[i] != index_k:
                            out.append(sorted([i,j,k]))
                    check[j] = index_j
        return out

        