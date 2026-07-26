class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        res = -1
        while (i!=j):
            mid = int((j + i) / 2)
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] > target:
                j = mid
            if nums[mid] < target:
                i = mid

            if i + 1 == j:
                if j < len(nums) and nums[j] == target:
                    res = j
                    break
                elif nums[i] == target:
                    res = i
                    break
                else :
                    break
        
         
        return res