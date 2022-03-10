class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth_list=[]
        for i in range(len(accounts)):
            l_sum=0
            accounts[i]=list(map(int,accounts[i]))
            l_sum=sum(accounts[i])
            wealth_list.append(l_sum)
        return max(wealth_list)