class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count = 0
        my_list = []
        for i in nums:
            if i ==1:
                one_count +=1
            else:
                my_list.append(one_count)
                one_count = 0
            if nums[-1] ==1:
                my_list.append(one_count)
        return max(my_list)

        