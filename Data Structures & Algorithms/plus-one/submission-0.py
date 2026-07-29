class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        extra = 0
        res = deque()
        for i in range(len(digits)-1,-1,-1):
            n = digits[i]
            if (i == len(digits)-1):
                n = n + 1
            else:
                n = n + extra
            
            if n > 9:
                extra = int(n / 10)
                val = int(n % 10)
            else:
                extra = 0
                val = n
            
            if n > 9 and i == 0:
                res.appendleft(val)
                res.appendleft(extra)
            else:
                res.appendleft(val)
                digits[i] = val
        return list(res)
            
        