import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=collections.Counter(nums)
        d=dict(freq)
        for key,value  in d.items():
            if value==1:
                return key
            else:
                pass