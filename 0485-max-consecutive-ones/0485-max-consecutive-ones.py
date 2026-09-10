class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_a=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                max_a=max(count,max_a)
            else:
                count=0
        return max_a
        