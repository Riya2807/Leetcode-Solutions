class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        elif needle=='':
            return 0
        elif needle in haystack:
            return haystack.find(needle[:])
        