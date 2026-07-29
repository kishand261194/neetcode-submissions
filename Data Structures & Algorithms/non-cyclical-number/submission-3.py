class Solution:
    def isHappy(self, n: int) -> bool:
        nstr = str(n)
        seen = set()
        ssum = 0
        while (ssum !=1): 
            ssum = 0  
            for i in nstr:
                ssum += int(i) ** 2
            if (ssum in seen):
                break          
            seen.add(ssum)
            nstr = str(ssum)

        return ssum == 1