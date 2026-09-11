class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        product_suf = 1
        product_pref = 1
        result= []

        for i in range(len(nums)):
            prefix.append(product_pref)
            product_pref *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            suffix.append(product_suf)
            product_suf*=nums[i]

        suffix.reverse()
        for i in range(len(nums)):

            result.append(suffix[i] * prefix[i])
        return result
            
        

        print(prefix)
        print(suffix)





        
            
        



        