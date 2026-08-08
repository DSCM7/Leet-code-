class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
        x = t
        for p in [2, 3, 5, 7]:
            while x % p == 0:
                x //= p
        if x != 1:
            return "-1"

        n = int(num)

        while True:
            s = str(n)

            if "0" not in s:          
                product = 1
                for ch in s:
                    product *= int(ch)

                if product % t == 0:
                    return s

            n += 1