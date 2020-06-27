class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for x in range(1,n+1):
            min_val=x
            y,sq=1,1
            while sq<=x:
                min_val=min(min_val,1+dp[x-sq])
                y+=1
                sq=y*y
            dp[x]=min_val
        return dp[n]
        
