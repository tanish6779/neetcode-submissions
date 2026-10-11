class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(len(nums)): 
            for j in range(i): #j is before i
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        #initially dp is 1 for all so we check if i (next number to j) is greater, if it is we check dp[i] and take the max between its dp and the dp of previous element + 1 (plus one is for current) and we return the max dp