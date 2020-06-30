class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(a):
            z=1
            for i in range(1,a+1):
               z*=i
            return z
        m=m-1
        n=n-1
        s=m+n
        s=fact(s)
        m=fact(m)
        n=fact(n)
        return s//(m*n)
