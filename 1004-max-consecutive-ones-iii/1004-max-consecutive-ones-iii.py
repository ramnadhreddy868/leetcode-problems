class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        zero_count=0
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            if i-l+1>max_len:
                max_len=i-l+1
        return max_len
                  