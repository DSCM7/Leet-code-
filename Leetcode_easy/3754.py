class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        st = ""

        if "0" not in s:
            x = n
        else:
            for ch in s:
                if ch != "0":
                    st += ch
            if st == "":      # all digits were zero
                return 0
            x = int(st)

        t = x
        digit_sum = 0

        while t != 0:
            d = t % 10
            digit_sum += d
            t //= 10

        return x * digit_sum