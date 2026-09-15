class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        r = k * threshold
        w = sum(arr[:k])
        count = 0

        if w >= r:
            count += 1

        for i in range(k, len(arr)):
            w += arr[i] - arr[i-k]

            if w >= r:
                count += 1

        return count