class Solution:
    def numTrees(self, n: int) -> int:
        if n<2: return 1
        sol=[0]*(n+1)
        sol[0],sol[1]=1,1
        for i in range(2,n+1):
            for j in range(0,i):
                sol[i]+=sol[j]*sol[i-j-1]
        return sol[n]
        
