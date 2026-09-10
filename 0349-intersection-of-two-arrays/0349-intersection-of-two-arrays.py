class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        left=0
        right=0
        n1=len(nums1)
        n2=len(nums2)
        i=[]
        while left<n1 and right<n2:

            if nums1[left] < nums2[right]:
                left += 1

            elif nums1[left] > nums2[right]:
                right += 1
            else :
                if not i or i[-1]!=nums1[left]:
                    i.append(nums1[left])
                left+=1
                right+=1
        return i
