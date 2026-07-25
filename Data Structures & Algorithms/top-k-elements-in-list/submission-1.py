class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        for i in range(len(nums)+1):
            topK.append(set())

        for i in nums:
            topK[frequency[i]].add(i)
            
        res = []

        for i in range(len(topK) -1 , -1, -1):
            if len(topK[i])!=0 and k > 0:
                while (k>0 and len(topK[i])!=0):
                     res.append(topK[i].pop())
                     k = k - 1
            if k == 0:
                break

        return res