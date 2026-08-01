class Solution:
    def sumZero(self, n: int):
        t = n // 2
        l = []

        for i in range(1, t + 1):
            l.append(-i)
            l.append(i)

        if n % 2 != 0:
            l.append(0)

        return l