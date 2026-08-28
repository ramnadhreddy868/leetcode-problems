class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        news = ""

        for char in s:
            if char.isalnum():
                news += char

        s = news
        def Palindrome(left,right):
            if left>=right:
                return True
            if s[left]!=s[right]:
                return False
            return Palindrome(left+1,right-1)
        return Palindrome(0,len(s)-1)