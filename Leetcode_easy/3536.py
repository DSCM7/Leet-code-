class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        l = []

        for i in s:
            l.append(int(i))

        l.sort()
        return l[-1] * l[-2]