class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        max = 1

        while i <= nums[0]:
            if nums[0] % i == 0 and nums[-1] % i == 0:
                if i > max:
                    max = i
            i += 1

        return max