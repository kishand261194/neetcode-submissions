import heapq
class KthLargest:
    k: int 
    nums: List[int]
    def __init__(self, n: int, nums1: List[int]):
        self.k = n
        self.nums = []

        for num in nums1:
            heapq.heappush(self.nums, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        temp = []
        for i in range(self.k):
            temp.append(heapq.heappop(self.nums))

        maxk = temp[-1]
        for i in range(len(temp)):
            heapq.heappush(self.nums, temp[i])
        return -maxk
        
