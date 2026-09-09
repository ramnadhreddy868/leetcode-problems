class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        l=0
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l1=0
        r1=k-1
        while l1<r1:
            nums[l1],nums[r1]=nums[r1],nums[l1]
            l1+=1
            r1-=1
        left=k
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

    
