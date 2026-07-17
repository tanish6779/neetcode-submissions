class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numset = set(nums)
        
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                current = nums[i]
                length = 1
                while current + 1 in numset:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
            
        
 

                


                

                
