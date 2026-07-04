class Solution:
    def climbStairs(self, n: int) -> int:
        # state: climb(i) = number of ways to climb to the top starting from step i
        # climb(i) = climb(i+1) + climb(i+2)
        memo = {}
        def climb(i):
            # base case 1: complete climb
            if i == n:
                return 1
            # base case 2: invalid over step
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]
        return climb(0)