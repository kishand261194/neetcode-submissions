class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        
        for c in s:
            if c.isalnum():
                cleanS += c.lower()

        reverse = cleanS[::-1]
        return reverse == cleanS

