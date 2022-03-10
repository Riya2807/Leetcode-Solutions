class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set()
        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)
			