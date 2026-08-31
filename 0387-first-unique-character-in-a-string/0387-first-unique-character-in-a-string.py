class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for char in s:
            if char in hash:
                hash[char]+=1
            else:
                hash[char]=1
        for index, char in enumerate(s):
            if hash[char]==1:
                return index
        return -1
        