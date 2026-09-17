class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_len=len(nums)+1
        w=0
        for i in range(len(nums)):
            w+=nums[i]
            while w>=target:
                if i-l+1<min_len:
                    min_len=i-l+1
                w-=nums[l]
                l+=1
        if min_len==len(nums)+1:
            return 0
        return min_len