import heapq

class Solution:
    def lastStoneWeight(self, stones1: List[int]) -> int:
        stones = []
        
        for i in stones1:
            heapq.heappush(stones, -i)

        while(len(stones) > 1):
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if (stone1 == stone2):
                continue
            elif (stone1 > stone2):
                heapq.heappush(stones, -(stone1-stone2))
            elif (stone1 < stone2):
                heapq.heappush(stones, -(stone2-stone1))        
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0