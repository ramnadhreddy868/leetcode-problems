class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max=window_sum
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            if window_sum>max:
                max=window_sum
        return max/k