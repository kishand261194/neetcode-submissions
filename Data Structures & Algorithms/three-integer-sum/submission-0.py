class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            target = nums[i]
            start = i + 1
            end = len(nums)-1
            while (start<end):
                if (nums[start] + nums[end] + target == 0):
                    tmp = sorted([nums[i],nums[start],nums[end]])
                    if tmp not in res:
                        res.append(tmp)
                    start=start+1
                    end=end-1
                elif(nums[start] + nums[end] + target > 0):
                    end=end-1
                elif(nums[start] + nums[end] + target < 0):
                    start=start+1

        return res