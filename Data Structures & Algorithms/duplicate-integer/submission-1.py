class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else: 
                map[i] += 1
        
        for i in map:
            if map[i] > 1:
                return True
        return False

    
        