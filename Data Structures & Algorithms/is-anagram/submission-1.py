class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfrequency = {}
        tfrequency = {}

        slen = len(s)
        tlen = len(t)

        if slen != tlen:
            return False

        for i in s:
            if i in sfrequency:
                sfrequency[i] += 1
            else:
                sfrequency[i] = 1
        
        for i in t:
            if i in tfrequency:
                tfrequency[i] += 1
            else:
                tfrequency[i] = 1
        
        for i in tfrequency:
            if not(i in sfrequency):
                return False

            if tfrequency[i] != sfrequency[i]:
                return False

        for i in sfrequency:
            if not(i in tfrequency):
                return False

            if sfrequency[i] != tfrequency[i]:
                return False

        return True