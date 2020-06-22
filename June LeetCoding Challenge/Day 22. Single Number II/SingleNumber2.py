class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp={}
        for item in nums:
            mp[item] = 1 if item not in mp else mp[item] + 1
        for key in mp:
            if mp[key] == 1 :
                return key
