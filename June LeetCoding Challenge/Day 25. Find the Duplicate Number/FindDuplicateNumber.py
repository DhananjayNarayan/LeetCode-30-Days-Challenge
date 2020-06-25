class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        return (sum(nums)-sum(set_nums))//(len(nums)-len(set_nums))
