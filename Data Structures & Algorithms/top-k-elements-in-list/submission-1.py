class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==2 and nums[0] == nums[1]:
            return [nums[0]]

        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] +=1
        return_list = []
        
        sorted_dict = sorted(hash.items(), key=lambda kv: kv[1], reverse=True)
        for i,m in sorted_dict[:k]:
            return_list.append(i)
        return return_list
            





                


        