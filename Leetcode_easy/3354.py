class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        i = n

        while True:
            p = 1
            temp = i

            while temp > 0:
                d = temp % 10
                p *= d
                temp //= 10

            if p % t == 0:
                return i

            i += 1