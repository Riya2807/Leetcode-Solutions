class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for t in range(0,n-1):  
            for j in range(n-1):  
                if(nums[j]>nums[j+1]):  
                    temp = nums[j]  
                    nums[j] = nums[j+1]  
                    nums[j+1] = temp  
        return nums
        