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

