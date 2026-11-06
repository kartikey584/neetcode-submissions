class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        pre = [0] * n
        suf = [0] * n

        pre[0] = 1
        pre[1] = nums[0]
        suf[n-1] = 1
        suf[n-2] = nums[n-1]

        for i in range(2,n):

            pre[i] = pre[i-1] * nums[i-1]
            suf[n-1-i] = suf[n-i] * nums[n-i]
        
        return list(map(lambda x, y: x * y, pre, suf))

