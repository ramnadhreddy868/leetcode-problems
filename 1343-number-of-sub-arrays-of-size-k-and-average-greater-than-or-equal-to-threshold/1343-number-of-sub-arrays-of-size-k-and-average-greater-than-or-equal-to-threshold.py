class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        w=sum(arr[:k])
        count=0
        if w>=k * threshold:
            count+=1
        for i in range(k,len(arr)):
            w=w+arr[i]-arr[i-k]
            
            if w>=k * threshold:
                count+=1
        return count


        