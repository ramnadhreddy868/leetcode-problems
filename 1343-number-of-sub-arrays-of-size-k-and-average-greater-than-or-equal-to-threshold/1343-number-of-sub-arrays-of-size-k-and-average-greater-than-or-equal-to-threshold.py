class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        w=sum(arr[:k])
        count=0
        if w>=k * threshold:
            count+=1
        for i in range(k,len(arr)):
            w-=arr[i-k]
            w+=arr[i]
            if w>=k * threshold:
                count+=1
        return count


        