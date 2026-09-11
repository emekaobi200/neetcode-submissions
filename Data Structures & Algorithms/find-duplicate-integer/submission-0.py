class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dics = {}
        for num in nums:
            if num in dics:
                return num
            dics[num] = 1