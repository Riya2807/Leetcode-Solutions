class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        if target not in nums:
            return [-1,-1]
        elif target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    ans.append(i)
            if len(ans)==1:
                ans.append(ans[0])
                return ans
            elif len(ans)>1:
                return [ans[0],ans[-1]]