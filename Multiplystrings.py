class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def atoi(str):
            resultant = 0
            for i in range(len(str)):
                resultant = resultant * 10 + (ord(str[i]) - ord('0'))
            return resultant
        a=atoi(num1)
        b=atoi(num2)
        return str(a*b)