class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                
                if sum<target:
                    left+=1
                elif sum>target:
                    right-=1
                elif sum==target:
                    return sum
                if abs(sum - target) < abs(closest - target):
                    closest = sum
        return closest
                