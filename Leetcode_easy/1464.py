class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=0
        for i in range (len(nums)-1):
            for j in range(i+1,len(nums)):
                t=(nums[i]-1)*(nums[j]-1)
                if t>maxi:
                    maxi=t
        return maxi

