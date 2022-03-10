class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for j in range(len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[j]+nums[k]==target:
                        return [j,k]
                    else:
                        continue