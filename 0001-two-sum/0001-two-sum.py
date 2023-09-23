class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums[i+1:]:
                j = nums.index(complement, i+1)
                return [i, j]
                
        return []

