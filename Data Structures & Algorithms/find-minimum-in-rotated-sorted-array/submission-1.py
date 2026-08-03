class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 0 # we are not using min here but still i kept it, its of no use 
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2 # // gives floor division operator like 5/2 = 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
        return nums[low]
                




