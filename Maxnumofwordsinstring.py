class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_list=[]
        for i in range(len(sentences)):
            count=0
            count=len(sentences[i].split())
            max_list.append(count)
        return max(max_list)