class Solution:
    def mirrorDistance(self, n: int) -> int:
        t = n
        s = ""

        while t > 0:
            d = t % 10
            s = s + str(d)
            t = t // 10

        return abs(n - int(s))