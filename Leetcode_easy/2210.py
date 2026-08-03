class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set(nums)
        sum=0
        for i in s:
            if i>0:
                sum+=i
        if sum==0:
            sum=max(s)
        return sum