class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        res = []
        for i in range(len(nums)):
            diff[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in diff and i != diff[target - nums[i]]:
                res = [i, diff[target - nums[i]]]
                break
        return res

        