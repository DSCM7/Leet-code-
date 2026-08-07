class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 3:
            return nums[0] * nums[1] * nums[2]

        max_product = nums[0] * nums[1] * nums[2]

        for i in range(size - 2):
            p = nums[i] * nums[i+1] * nums[i+2]
            if p > max_product:
                max_product = p

        return max_product