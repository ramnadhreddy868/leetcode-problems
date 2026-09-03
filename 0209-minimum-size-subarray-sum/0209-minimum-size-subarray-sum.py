class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        windowsum=0
        minlength=float('inf')
        for right in range(len(nums)):
            windowsum+=nums[right]
            while windowsum>=target:
                current=right-left+1
                if current<minlength:
                    minlength=current
                windowsum-=nums[left]
                left+=1
        if minlength == float('inf'):
            return 0
        else:
            return minlength

        
            