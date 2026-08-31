class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_1={}
        hash_2={}
        for num in nums1:
            if num in hash_1:
                hash_1[num]+=1
            else:
                hash_1[num]=1
        for num in nums2:
            if num in hash_2:
                hash_2[num]+=1
            else:
                hash_2[num]=1
        
        result=[]
        for num in hash_2:
            if num in hash_1:
                if num not in result:
                   result+=[num]
                else:
                    result
        return result