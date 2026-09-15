class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=sum(nums[:k])
        maxsum=w
        for i in range(k,len(nums)):
            w=w+nums[i]-nums[i-k]
            if w>maxsum:
                maxsum=w
        return maxsum/k