class Solution:
    def climbStairs(self, n: int) -> int: #use dp array
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        #we use dp[i] = dp[i-1] + dp[i-2]
                        # one   + two
        #bottum up dp program we start with n as base case and move up
