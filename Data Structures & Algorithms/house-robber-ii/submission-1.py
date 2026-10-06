class Solution:
    def rob(self, nums: List[int]) -> int:
        #this question is the same as house robber1 but here the array is in a circle so the first and last elements cannot be added, so we can use the previous logic and take care of cases, removing first element, last element and for nums = 0 only 0
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    

    def helper(self, nums):
        rob1,rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        