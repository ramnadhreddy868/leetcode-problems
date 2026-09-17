class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        window_sum=0
        min_len=len(nums)+1
        for i in range(len(nums)):
            window_sum+=nums[i]
            while window_sum>=target:
                if i-l+1 < min_len:
                    min_len=i-l+1
                window_sum -= nums[l]
                l += 1
        if min_len==len(nums)+1 :
            return 0
        return min_len