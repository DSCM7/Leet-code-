class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        min=nums[0]
        max=nums[len(nums)-1]
        for i in range(min,max+1):
            if i not in nums:
                l.append(i)
        return l

        
    
                    
        
        