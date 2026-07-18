class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        ii = 0
        for i in nums: 
            diff[i] = ii
            ii += 1
        
        jj = 0
        for i in nums: 
            rdiff = target - i
            if rdiff in diff and jj != diff[rdiff]:
                return [jj, diff[rdiff]]
            jj += 1

        