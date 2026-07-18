class Solution:
    def isPalindrome(self, s: str) -> bool:
        charSet = set()
        for i in range(ord('A'),ord('Z')):
            charSet.add(i)

        for i in range(ord('a'),ord('z')):
            charSet.add(i)    

        for i in range(ord('0'),ord('9')):
            charSet.add(i) 

        result = True
        i = 0
        j = len(s) - 1 

        while (len(s) > 1 and i <= j):
            while (i < len(s)-1 and ord(s[i]) not in charSet):
                i+=1

            while (j > 0 and ord(s[j]) not in charSet):
                j-=1
            
            if (j < 1):
                break

            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                result = False
                break
        
        return result

