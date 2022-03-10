class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums, low, high, target):
            if low > high:
                return -1
            
            mid = (low+high)//2
            current = nums[mid]
            if current == target:
                return mid
            

            elif current > target:  
                high=mid - 1
                return binary_search(nums, low,high, target)
            
            elif current < target:  # search to the right
                low=mid+ 1
                return binary_search(nums,low,high, target)
    
        return binary_search(nums, 0, len(nums)-1, target)