class Solution:
    def rob(self, nums: List[int]) -> int:
        #[1,2,3,4,5]
        #[1,x,3,x,5]
        #[rob1,rob2,n,n,n]
        # we can only rob rob1 and n, we cannot rob2 as it is adjacent
        #temp = max(rob1+n, rob2)
        #rob1 = rob2
        #rob2 = temp

        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return temp

        #OTHER APPROACH
        #if len(nums) == 1:
        #return nums[0]
        #dp = [0] * len(nums)
        #dp[0] = nums[0]
        #dp[1] = max(nums[0], nums[1])
        #for i in range(2, len(nums)-1):
        #dp[i] = max(dp[i -2], nums[i] + dp[i-1])
        #return dp[-1] is the last element
        

