class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=list(s.strip().split())
        l2=l1[::-1]
        res=""
        for i in range(len(l2)):
            res+= l2[i]+" "
        return res.strip()