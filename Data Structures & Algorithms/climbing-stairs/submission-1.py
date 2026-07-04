class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up: how many ways to get to step i
        # dp[i] = dp[i-1] + dp[i-2]
        # handle n = 0 and 1
        if n <= 1:
            return 1
        # initialize dp array 
        dp = [0] * (n+1)
        
        # base cases
        dp[0] = 1
        dp[1] = 1
        # main loop from 2 to n
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]